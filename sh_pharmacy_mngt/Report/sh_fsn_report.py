from odoo import fields,models,api
import io
import base64
from odoo.exceptions import UserError
import xlsxwriter
# import xlwt
from datetime import datetime,date

  
class FsnReport(models.TransientModel):
    _inherit="sh.report.wizard"
    
    is_fsn_report=fields.Boolean()
    fsn_records_ids = fields.Many2many('fsn.report.data')
    fsn_product_id=fields.Many2one('product.product')
    fsn_category_id=fields.Many2one('product.category')
    min_qty=fields.Float()

    def load_fsn_record(self):
        print(f"\n\n\n\t--------------> 32 ", "fsn record called")
        self.fsn_records_ids=[(5,0,0)]

        if self.category_id:
            fsn_record=self.env['sale.report'].search([('product_id.categ_id','=',self.category_id.id),('date','>=',self.start),('date','<=',self.stop)])
        if self.product_id:
            fsn_record=self.env['sale.report'].search([('product_id','=',self.product_id.id),('date','>=',self.start),('date','<=',self.stop)])
        if not self.product_id and not self.category_id:
            fsn_record=self.env['sale.report'].search([('date','>=',self.start),('date','<=',self.stop)])
        vals_list = []

        for record in fsn_record:
            if record.product_uom_qty < self.min_qty:
                status = 'slow'
            else:
                status='fast'
            
            vals = {
                'product_id': record.product_id.id,
                'category_id': record.product_id.categ_id.id,
                'qty_sold': record.product_uom_qty,
                'stock_qty':record.product_id.qty_available,
                'forcast_qty':record.product_id.virtual_available,
                'sale_rate': status,
            }

            vals_list.append((0, 0, vals))

        self.fsn_records_ids = vals_list

        return {
            'type': 'ir.actions.act_window',
            'name': 'report list',
            'view_mode': 'form',
            'res_model': 'sh.report.wizard',
            'res_id': self.id,
            'target': 'new',
        }
        
        
    def fsn_export_exel(self):
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
            'Product', 'Category', 'Quantity Sold','Onhand quantity','Forcast Quantity','Sale Rate',
        ]
        header_format = workbook.add_format({'bold': True, 'bg_color': '#D3D3D3'})
        for col, title in enumerate(header):
            worksheet.write(2, col, title, header_format)

        row = 3
        count = 1
        col_widths = [len(title) for title in header]
        
        total_amount =0
        for rec in self.fsn_records_ids:
            # if not rec.product_id or not rec.lot_id or not rec.expiration_date or not rec.alert_date or not rec.product_qty or not rec.category_id :
            #     continue


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
                rec.product_id.name if rec.product_id else '',
                rec.category_id.name if rec.category_id else '',
                rec.qty_sold if rec.qty_sold is not None else '',
                rec.stock_qty if rec.stock_qty is not None else '',
                rec.forcast_qty if rec.forcast_qty is not None else '',
                rec.sale_rate if rec.sale_rate is not None else '',


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
