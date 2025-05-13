from odoo import fields,models,api
import io
import base64
from odoo.exceptions import UserError
import xlsxwriter
from datetime import datetime,date

class ExpiryReport(models.TransientModel):
    _inherit="sh.report.wizard"
    
    is_expiry_wise=fields.Boolean()
    product_id=fields.Many2one("product.product")
    category_id=fields.Many2one("product.category")
    lot_id=fields.Char()
    lot_no=fields.Many2one('stock.lot')
    category_id_domain=fields.Char()
    lot_domain=fields.Char(default="[(1,'=',1)]")
    expiration_record_ids=fields.Many2many('sh.expiry.report')
    
    def load_expiry_record(self):
        print(f"\n\n\n\t--------------> 10 ","expiry load called")
        self.expiration_record_ids=[(5,0,0)]

        if self.category_id:
            expiry_records=self.env['stock.quant'].search([('expiration_date','>=',self.start),('expiration_date','<=',self.stop),('product_id.categ_id','=',self.category_id.id),('location_id.usage', '=', 'internal')
])
        if self.product_id:
            expiry_records=self.env['stock.quant'].search([('expiration_date','>=',self.start),('expiration_date','<=',self.stop),('product_id','=',self.product_id.id),('location_id.usage', '=', 'internal')
])
        if self.lot_no:
            expiry_records=self.env['stock.quant'].search([('expiration_date','>=',self.start),('expiration_date','<=',self.stop),('lot_id','=',self.lot_no.name),('location_id.usage', '=', 'internal')
])
        if not self.product_id  and not self.lot_no and not self.category_id:
            expiry_records=self.env['stock.quant'].search([('expiration_date','>=',self.start),('expiration_date','<=',self.stop),('location_id.usage', '=', 'internal')
])
        
        for record in expiry_records:

                vals={
                    'product_id':record.product_id.id,
                    'expiry_lot_id':record.lot_id.id,
                    'expiration_date':record.expiration_date,
                    'alert_days':(record.expiration_date - datetime.today()).days,
                    'product_qty':record.available_quantity,
                    'category_id':record.product_id.categ_id.id,

                }
            
                self.expiration_record_ids=[(0,0,vals)]
        
        return{
            'type': 'ir.actions.act_window',
            'name': 'report list',
            'view_mode': 'form',
            'res_model': 'sh.report.wizard',
            'res_id':self.id,
            'target':'new',
        }
    
    @api.onchange('product_id')
    def change_product2(self):
        self.category_id=self.product_id.categ_id.id
        print(f"\n\n\n\t--------------> 65 nnnnnn",)
        if self.product_id:
            self.lot_domain="[('product_id','=',"+str(self.product_id.id)+")]"
        else:
            self.lot_domain = "[(1,'=',1)]"
            
    
    
    @api.onchange('category_id')
    def change_category2(self):
        if self.category_id:
            self.category_id_domain = "[('categ_id','=',"+str(self.category_id.id)+")]"
        else:
            self.category_id_domain = "[(1,'=',1)]"
     
     
    @api.onchange('lot_no')
    def change_lot2(self):
        if self.lot_no:
            self.product_id=self.lot_no.product_id.id

     
    def expiry_export_exel(self):


        
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
            'Product', 'Lot', 'Expiration Date','Remaining days','Quantity','Category',
        ]
        header_format = workbook.add_format({'bold': True, 'bg_color': '#D3D3D3'})
        for col, title in enumerate(header):
            worksheet.write(2, col, title, header_format)

        row = 3
        count = 1
        col_widths = [len(title) for title in header]
        
        total_amount =0
        for rec in self.expiration_record_ids:


            values = [
                rec.product_id.name if rec.product_id else '',
                rec.expiry_lot_id.name or '',
                rec.expiration_date.strftime("%d/%m/%Y") if rec.expiration_date else '',
                (rec.expiration_date-datetime.today() ).days if rec.expiration_date else '',
                rec.product_qty if rec.product_qty is not None else '',
                rec.category_id.name if rec.category_id else '',
            ]

            for col, val in enumerate(values):
                worksheet.write(row, col, val)
                col_widths[col] = max(col_widths[col], len(str(val)))


            row += 1
            count += 1

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
        
        




