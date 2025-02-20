from odoo import fields,api,models

class Note(models.Model):
    # _name="sh.note"
    # _description="this table is used to manage notes"
    _inherit="sale.order"

    note=fields.Char()
    # games=fields.Many2many()