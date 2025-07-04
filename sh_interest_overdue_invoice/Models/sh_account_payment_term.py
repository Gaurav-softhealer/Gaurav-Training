from odoo import fields, models

class AccountPaymentTerm(models.Model):
    _inherit = 'account.payment.term'

    sh_interest_rate = fields.Float(string="Interest Rate (%)", help="Annual interest rate for overdue invoices.")
    sh_interest_type = fields.Selection([
        ('daily', 'Daily'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
    ], string="Interest Type", default='daily', help="Period for interest calculation.")
    sh_interest_account_id = fields.Many2one('account.account', string="Interest Account", help="Account for posting interest journal entries.")
