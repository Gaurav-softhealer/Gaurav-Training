from odoo import fields,models,api
import io
import base64
from odoo.exceptions import UserError
import xlsxwriter
# import xlwt
from datetime import datetime,date

class CommissionReport(models.TransientModel):
    _inherit="sh.report.wizard"
    
    is_commission=fields.Boolean()
    dr_id=fields.Many2one('res.partner',domain=[('is_doctor','=',True)])
    dr_commission_ids=fields.Many2many('sh.doctor.commission')
    
    def load_commission_record(self):
        print(f"\n\n\n\t--------------> 11 ","load commission button called")
        if self.dr_id:
            commission_record=self.env['sh.doctor.commission'].search([('date','>=',self.start),('date','<=',self.stop),('sh_doctor_id','=',self.dr_id.id)])
        else:
            commission_record=self.env['sh.doctor.commission'].search([('date','>=',self.start),('date','<=',self.stop)])
        
        record_ids=commission_record.ids
        self.dr_commission_ids=[(6,0,record_ids)]
        return{
            'type': 'ir.actions.act_window',
            'name': 'report list',
            'view_mode': 'form',
            'res_model': 'sh.report.wizard',
            'res_id':self.id,
            'target':'new',
        } 
        
    def commission_export_exel(self):
        print(f"\n\n\n\t--------------> 29 ","commission export")
        
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
            'Date', 'Order No', 'Patient','Doctor','Amount','Commission Type','Commission Rate','Commission Amount',
        ]
        header_format = workbook.add_format({'bold': True, 'bg_color': '#D3D3D3'})
        for col, title in enumerate(header):
            worksheet.write(2, col, title, header_format)

        row = 3
        count = 1
        col_widths = [len(title) for title in header]
        
     
        for rec in self.dr_commission_ids:



            # if rec.state == 'cancel':
            #     values = [
            #         str(count),
            #         rec.name,
            #         '', '', '', '', '',
            #         '-',
            #         'CANCELLED ',
            #         '', '', '', '', '', '', '', '-', ''
            #     ]
            # else:
                

            values = [
                rec.date.strftime("%d/%m/%Y") if rec.date else '',
                rec.sh_so_id.name if rec.sh_so_id else '',
                rec.patient_id.name if rec.patient_id else '',
                rec.sh_doctor_id.name if rec.sh_doctor_id else '',
                rec.sh_so_amount if rec.sh_so_amount else '',
                rec.doctor_commission_type if rec.doctor_commission_type else '',
                rec.commission_rate if rec.commission_rate else '',
                rec.dr_commission if rec.dr_commission else '',
                
                
            ]
                # total_amount +=rec.amount_total

            # Write values and update column widths
            for col, val in enumerate(values):
                worksheet.write(row, col, val)
                col_widths[col] = max(col_widths[col], len(str(val)))


            row += 1
            count += 1

        # worksheet.write(row, 3, 'TOTAL', bold_style)
        # worksheet.write(row, 4, total_amount, num_format)
 

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
