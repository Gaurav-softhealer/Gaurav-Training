from odoo import fields,models,api

class Custom(models.Model):
    _inherit="sale.order"
    
    note_ids=fields.Many2many("sh.note",string="Notes")
