from odoo import fields,models

class SaleAutoWork(models.Model):
    _name="sh.sale.auto.workflow"
    _description="This model is used to manage sale auto workflow"
    
    name=fields.Char()
    
    delivery_order=fields.Boolean()
    create_invoice=fields.Boolean()
    force_transfer=fields.Boolean()
    validate_invoice=fields.Boolean()
    register_payment=fields.Boolean()
    send_email=fields.Boolean(string="Send Invoice By Email")
    sale_journal=fields.Many2one('account.journal',domain=[('type','=','sale')])
    sh_payment_journal=fields.Many2one('account.journal',domain=[('type','in',('bank','cash'))])
    payment_method=fields.Many2one('account.payment.method')
    company_id=fields.Many2one('res.company')
    
    