from odoo import fields,models,api
from datetime import datetime,timedelta
import io
import base64
from odoo.exceptions import UserError
import xlsxwriter
import xlwt

class ReportWizard(models.TransientModel):
    _name="sh.report.wizard"
    _description="this model is for report wizard"
    
    patient_id=fields.Many2one('res.partner',string="Patient Name",domain=[('is_patient','=',True)])
    

    
    
    start = fields.Datetime(
        'Start',  tracking=True,
        help="Start date of an event, without time for full days events")
    
    stop = fields.Datetime(
        'Stop',  tracking=True, 
         readonly=False, store=True,
        help="Stop date of an event, without time for full days events")
    
    start_date = fields.Date(
        'Start Date', store=True, tracking=True,
        )
    
    stop_date = fields.Date(
        'End Date', store=True, tracking=True,
        )
    is_patient_wise = fields.Boolean()
    patient_record_ids=fields.Many2many('sale.order')
    
    sh_gender=fields.Selection([
        ('male','Male'),
        ('female','Female')
    ],string="Gender")
    
    age=fields.Integer()

    def load_data(self,record_ids):
        print(f"\n\n\n\t--------------> 36 ","load data")
        if self.is_patient_wise:
            if self.age:
                patient_record=self.env['sale.order'].search([('partner_id.sh_age','=',self.age),('date_order','>=',self.start),('date_order','<=',self.stop)])
            if self.sh_gender:
                patient_record=self.env['sale.order'].search([('partner_id.gender','=',self.sh_gender),('date_order','>=',self.start),('date_order','<=',self.stop)])
            if self.patient_id:
                patient_record=self.env['sale.order'].search([('partner_id','=',self.patient_id.id),('date_order','>=',self.start),('date_order','<=',self.stop)])
            if not self.patient_id and not self.sh_gender and not self.age:
                patient_record=self.env['sale.order'].search([('date_order','>=',self.start),('date_order','<=',self.stop)])
                
            print(f"\n\n\n\t--------------> 38 patient_record",patient_record)
            record_ids=patient_record.ids
        self.patient_record_ids=[(6,0,record_ids)]
        return{
            'type': 'ir.actions.act_window',
            'name': 'report list',
            'view_mode': 'form',
            'res_model': 'sh.report.wizard',
            'res_id':self.id,
            'target':'new',
        }  
    
    @api.onchange('patient_id')
    def change_patient(self):
        self.sh_gender=self.patient_id.gender
        
    # @api.onchange('sh_gender')
    # def change_gender(self):
    #     if self.sh_gender:
    #         self.patient_domain="[('gender','=',"+str(self.sh_gender)+")]"
    #     else:
    #         self.patient_domain = "[(1,'=',1)]"
    
       
    def print_record_exel(self):
        print(f"\n\n\n\t--------------> 35 ","display records")
            
        
        workbook = xlwt.Workbook(encoding='utf-8')

        
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet("Invoices")

        bold_style = workbook.add_format({'bold': True,'align': 'center','valign': 'vcenter','border': 1})
        num_format = workbook.add_format({'num_format': '#,##0.00','align': 'right','valign': 'vcenter','border': 1})
        worksheet.merge_range('A1:R1', 'Patient wise Report', workbook.add_format({
            'bold': True,
            'font_size': 14,
            'align': 'center',
            'valign': 'vcenter'
        }))
        date_range = f'From: {self.start.strftime("%d/%m/%Y")} To: {self.stop.strftime("%d/%m/%Y")}'
        worksheet.merge_range('A2:R2', date_range, workbook.add_format({
            'font_size': 11,
            'align': 'center',
            'valign': 'vcenter'
        }))

        header = [
            'NO.', 'ORDER DATE', 'CUSTOMER','SALESPERSON','TOTAL',
        ]
        header_format = workbook.add_format({'bold': True, 'bg_color': '#D3D3D3'})
        for col, title in enumerate(header):
            worksheet.write(2, col, title, header_format)

        row = 3
        count = 1
        col_widths = [len(title) for title in header]
        
        total_amount =0
        for rec in self.patient_record_ids:
            if not rec.name or not rec.date_order or not rec.partner_id.name or not rec.user_id.name or not rec.amount_total:
                continue


            if rec.state == 'cancel':
                values = [
                    str(count),
                    rec.name,
                    '', '', '', '', '',
                    '-',
                    'CANCELLED ',
                    '', '', '', '', '', '', '', '-', ''
                ]
            else:
                

                values = [
                    rec.name,
                    rec.date_order.strftime("%d/%m/%Y"),
                    rec.partner_id.name,
                    rec.user_id.name,
                    rec.amount_total,
                    
                ]
                total_amount +=rec.amount_total

            # Write values and update column widths
            for col, val in enumerate(values):
                worksheet.write(row, col, val)
                col_widths[col] = max(col_widths[col], len(str(val)))

            row += 1
            count += 1

        worksheet.write(row, 3, 'TOTAL', bold_style)
        worksheet.write(row, 4, total_amount, num_format)
 

        # Apply final column widths
        for col, width in enumerate(col_widths):
            worksheet.set_column(col, col, width + 2)  # +2 for padding

        fp = io.BytesIO()
        workbook.close()
        output.seek(0)
        xlsx_data = base64.b64encode(output.read())
        IrAttachment = self.env['ir.attachment']
        attachment_vals = {
            'name': 'Patient wise Report.xls',
            'res_model': 'ir.ui.view',
            'type': 'binary',
            'datas': xlsx_data,
            'public': True,
            }
        fp.close()

        attachment = IrAttachment.search([('name', '=',
                'Invoice Payment Report.xls'), ('type', '=', 'binary'),
                ('res_model', '=', 'ir.ui.view')], limit=1)
        if attachment:
            attachment.write(attachment_vals)
        else:
            attachment = \
                IrAttachment.create(attachment_vals)
        if not attachment:
            raise UserError('There is no attachments...')

        url = '/web/content/' + str(attachment.id) \
            + '?download=true'
        return {'type': 'ir.actions.act_url', 'url': url,
                'target': 'new'}

 