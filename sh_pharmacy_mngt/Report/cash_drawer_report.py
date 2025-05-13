from odoo import fields,models,api
import io
import base64
from odoo.exceptions import UserError
import xlsxwriter
# import xlwt
from datetime import datetime,date


class CashDrawerData(models.Model):
    _name="cash.drawer.data"
    _description="this models is used to store data about cash drawer"
    
    date=fields.Datetime(string="Date")
    cashier_id=fields.Many2one('res.users')
    opening_bal=fields.Float()
    closing_bal=fields.Float()
    card_amount=fields.Float()
    cash_amount=fields.Float()
    upi_amount=fields.Float()
    total=fields.Float()
    payment_method=fields.Many2one('pos.payment')
    
    


class CashDrawer(models.TransientModel):
    _inherit="sh.report.wizard"
    
    cashier_id=fields.Many2one('res.users')
    is_cash_drawer=fields.Boolean()
    cash_drawer_records_ids = fields.Many2many('cash.drawer.data')

    
    def load_cash_drawer_record(self):
        print(f"\n\n\n\t--------------> 17 ","cashier callled")
        self.cash_drawer_records_ids=[(5,0,0)]
        
        if self.cashier_id:
            cash_drawer_record=self.env['pos.session'].search([('start_at','>=',self.start),('start_at','<=',self.stop),('user_id','=',self.cashier_id.id)])
        else:
            cash_drawer_record=self.env['pos.session'].search([('start_at','>=',self.start),('start_at','<=',self.stop)])
            # payment_record=self.env['pos.payment'].search([('payment_date','=',self.start)])
        opening=0
        closing=0   
        cash_amount=0
        card_amount=0
        upi_amount=0
        for record in cash_drawer_record:
            for order in record.order_ids:
                for payment in order.payment_ids:
                    method_name = payment.payment_method_id.name.lower()
                    if 'cash' in method_name:
                        cash_amount += payment.amount
                    elif 'card' in method_name:
                        card_amount += payment.amount
                    elif 'upi' in method_name:
                        upi_amount += payment.amount

                    vals={
                        'date':record.start_at,
                        'cashier_id':record.user_id.id,
                        'opening_bal':record.cash_register_balance_start,
                        'closing_bal':record.cash_register_balance_end_real,
                        'cash_amount':cash_amount,
                        'card_amount':card_amount,
                        'upi_amount':upi_amount
                        # 'payment_method':i.id
                    }
            
                    self.cash_drawer_records_ids=[(0,0,vals)]
        return{
            'type': 'ir.actions.act_window',
            'name': 'report list',
            'view_mode': 'form',
            'res_model': 'sh.report.wizard',
            'res_id':self.id,
            'target':'new',
        } 
        
    def cash_drawer_export_exel(self):
        print(f"\n\n\n\t--------------> 36 ","cash drawer export report")
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
            'Date', 'Cashier', 'Opening Balance','Closing Balance','Cash Amount','Card Amount','UPI Amount',
        ]
        header_format = workbook.add_format({'bold': True, 'bg_color': '#D3D3D3'})
        for col, title in enumerate(header):
            worksheet.write(2, col, title, header_format)

        row = 3
        count = 1
        col_widths = [len(title) for title in header]
        
        total_amount =0
        for rec in self.cash_drawer_records_ids:

            values = [
                rec.date.strftime("%d/%m/%Y") if rec.date else '',
                rec.cashier_id.name if rec.cashier_id else '',
                rec.opening_bal if rec.opening_bal is not None else '',
                rec.closing_bal if rec.closing_bal is not None else '',
                rec.cash_amount if rec.cash_amount is not None else '',
                rec.card_amount if rec.card_amount is not None else '',
                rec.upi_amount if rec.upi_amount is not None else '',


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

