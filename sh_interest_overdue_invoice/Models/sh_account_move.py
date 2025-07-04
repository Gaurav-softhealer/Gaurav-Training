from odoo import fields, models, api
from datetime import date   
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError,ValidationError

class AccountMove(models.Model):
    _inherit = 'account.move'

    sh_interest_amount = fields.Monetary(string="Interest Amount", currency_id=lambda self: self.env.company.currency_id)
    sh_original_amount = fields.Monetary(string="Original Amount", currency_id=lambda self: self.env.company.currency_id)
    invoice_line_ids = fields.One2many(  # /!\ invoice_line_ids is just a subset of line_ids.
        'account.move.line',
        'move_id',
        string='Invoice lines',                                                                                                                     
        copy=False,
        domain=[('is_interest_line','=',False),('display_type', 'in', ('product', 'line_section', 'line_note',))],
    ) 
    is_update=fields.Boolean(default=False)
    is_reset=fields.Boolean(default=False)

    def cron_interest_overdue_invoice(self):
        print(f"\n\n\n\t--------------> 27 ","cron called")
        today = date.today()
        print(f"\n\n\n\t--------------> 29 today",today)

        invoices = self.search([
            ('state', '=', 'draft'),
            ('move_type', '=', 'out_invoice'),
            ('invoice_date_due', '!=', False),
        ])

        for record in invoices:
            print(f"\n\n\n\t--------------> 27 record", record)
            if not record.sh_original_amount:
                record.sh_original_amount = sum(line.price_subtotal for line in record.invoice_line_ids)
            base_amount = record.sh_original_amount
            interest = 0

            days_overdue = (today - record.invoice_date_due).days
            month_overdue = relativedelta(today, record.invoice_date_due).months
            year_overdue = relativedelta(today, record.invoice_date_due).years

            if record.invoice_payment_term_id and record.invoice_payment_term_id.sh_interest_rate:
                print(f"\n\n\n\t--------------> 47 value set")
                rate = record.invoice_payment_term_id.sh_interest_rate / 100

                if record.invoice_payment_term_id.sh_interest_type == 'daily':
                    interest = base_amount * rate * days_overdue
                elif record.invoice_payment_term_id.sh_interest_type == 'monthly':
                    interest = base_amount * rate * (month_overdue + 1)
                elif record.invoice_payment_term_id.sh_interest_type == 'yearly':
                    interest = base_amount * rate * (year_overdue + 1)

                record.sh_interest_amount += interest
                
                print(f"\n\n\n\t--------------> 56 record.sh_interest_amount",record.sh_interest_amount)
                print(f"\n\n\n\t--------------> 61 record.id",record.id)
                print(f"\n\n\n\t--------------> 62 ",record.invoice_payment_term_id.sh_interest_account_id.id)
                
                interest_entry_exist=self.env['account.move.line'].search([('move_id','=',record.id),('name','=',"Interest Entry"),('account_id','=',record.invoice_payment_term_id.sh_interest_account_id.id)])
                if interest_entry_exist:
                    interest_entry_exist.write({
                        'move_id':record.id,
                        'name': 'Interest Entry',
                        'account_id': record.invoice_payment_term_id.sh_interest_account_id.id,
                        'price_unit': record.sh_interest_amount,
                        'quantity': 1,
                        'debit': 0.0,
                        'credit': record.sh_interest_amount,
                        'partner_id': record.partner_id.id,
                        'is_interest_line': True,  
                    })
                else:
                    self.env['account.move.line'].create({
                        'move_id':record.id,
                        'name': 'Interest Entry',
                        'account_id': record.invoice_payment_term_id.sh_interest_account_id.id,
                        'price_unit': record.sh_interest_amount,
                        'quantity': 1,
                        'debit': 0.0,
                        'credit': record.sh_interest_amount,
                        'partner_id': record.partner_id.id,
                        'is_interest_line': True,   
                    })
        

    def action_update_interest(self):
        print(f"\n\n\n\t--------------> 16 update called",)
        print(f"\n\n\n\t--------------> 29 is_update",self.is_update)

        print(f"\n\n\n\t--------------> 31 is_update",self.is_update)
        for record in self:
            if not record.sh_original_amount:
                record.sh_original_amount = sum(line.price_subtotal for line in record.invoice_line_ids)
            base_amount = record.sh_original_amount
            
            if record.is_update:
                if record.invoice_payment_term_id.sh_interest_type == 'daily':
                    raise ValidationError("Your payment term is daily , and you can update it only once in day")
                if record.invoice_payment_term_id.sh_interest_type == 'monthly':
                    raise ValidationError("Your payment term is monthly , and you can update it only once in month")
                if record.invoice_payment_term_id.sh_interest_type == 'yearly':
                    raise ValidationError("Your payment term is yearly , and you can update it only once in year")

            interest=0
            today=date.today()
            days_overdue = (today - record.invoice_date_due).days
            month_overdue=  relativedelta(today, record.invoice_date_due).months
            year_overdue=relativedelta(today, record.invoice_date_due).years
            print(f"\n\n\n\t--------------> 30 ",month_overdue)
            print(f"\n\n\n\t--------------> 31 ",year_overdue)
            # print(f"\n\n\n\t--------------> 26 round(0.5)",math.ceil(0.5))
            # print(f"\n\n\n\t--------------> 26 days_overdue",days_overdue)
            if today > record.invoice_date_due:
                interest_rate=(record.invoice_payment_term_id.sh_interest_rate/100)
                if record.invoice_payment_term_id.sh_interest_type == 'daily':
                    interest=base_amount*interest_rate*days_overdue
                if record.invoice_payment_term_id.sh_interest_type == 'monthly':
                    interest=base_amount*interest_rate*(month_overdue+1)
                if record.invoice_payment_term_id.sh_interest_type == 'yearly':
                    interest=base_amount*interest_rate*(year_overdue+1)
                print(f"\n\n\n\t--------------> 120 interest_value",interest)
                record.sh_interest_amount+=interest
                
                interest_entry_exist=self.env['account.move.line'].search([('move_id','=',record.id),('name','=',"Interest Entry"),('account_id','=',record.invoice_payment_term_id.sh_interest_account_id.id)])
                if interest_entry_exist:
                    interest_entry_exist.write({
                        'move_id':self.id,
                        'name': 'Interest Entry',
                        'account_id': self.invoice_payment_term_id.sh_interest_account_id.id,
                        'price_unit': self.sh_interest_amount,
                        'quantity': 1,
                        'debit': 0.0,
                        'credit': self.sh_interest_amount,
                        'partner_id': self.partner_id.id,
                        'is_interest_line': True,   
                    })

                    record.is_update = True
                else:
                    self.env['account.move.line'].create({
                        'move_id':self.id,
                        'name': 'Interest Entry',
                        'account_id': self.invoice_payment_term_id.sh_interest_account_id.id,
                        'price_unit': self.sh_interest_amount,
                        'quantity': 1,
                        'debit': 0.0,
                        'credit': self.sh_interest_amount,
                        'partner_id': self.partner_id.id,
                        'is_interest_line': True,   
                    })
                    record.is_update = True

            
    def action_reset_interest(self):
        print(f"\n\n\n\t--------------> 16 reset called",)
        for record in self:
            interest_lines = record.line_ids.filtered(lambda l: l.is_interest_line)
            if record.is_reset:
                if record.invoice_payment_term_id.sh_interest_type == 'daily':
                    raise ValidationError("Your payment term is daily , and you can reset it only once in day")
                if record.invoice_payment_term_id.sh_interest_type == 'monthly':
                    raise ValidationError("Your payment term is monthly , and you can reset it only once in month")
                if record.invoice_payment_term_id.sh_interest_type == 'yearly':
                    raise ValidationError("Your payment term is yearly , and you can reset it only once in year")

            interest_lines.unlink()
            record.sh_interest_amount = 0.0

            record.is_reset = True
        
    

   
class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    is_interest_line = fields.Boolean(string="Interest Line", default=False)    

            
            
            
            
            
            
            
            
            
    