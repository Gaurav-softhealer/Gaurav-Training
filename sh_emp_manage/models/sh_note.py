from odoo import fields,api,models

class Note(models.Model):
    _inherit="sale.order"

    note=fields.Char()