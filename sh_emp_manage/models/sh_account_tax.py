from odoo import fields,models

class Account(models.Model):
    _name="sh.account.tax"
    _description="this table is store data about account tax"
    
    name=fields.Char()
    tax=fields.Integer()
    
    sale_order_lines=fields.Many2many('sh.sale.order.line')