from odoo import fields,api,models

class Inheritance(models.Model):
    _inherit="sh.library.book"

    game=fields.Char()