from odoo import fields,models,api

class OrderLine(models.Model):
    _inherit="sale.order.line"
    
    note_ids=fields.Many2many("sh.note",string="Notes")