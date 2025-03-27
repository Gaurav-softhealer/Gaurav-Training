from odoo import fields,models

class SaleAutoWork(models.Model):
    _name="sh.sale.auto.workflow"
    _description="This model is used to manage sale auto workflow"
    
    name=fields.Char()
    
    delivery_order=fields.Boolean()
    create_invoice=fields.Boolean()
    validate_invoice=fields.Boolean()
    register_payment=fields.Boolean()
    send_email=fields.Boolean(string="Send Invoice By Email")
    
    