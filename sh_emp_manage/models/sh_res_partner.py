from odoo import fields,models

class Partner(models.Model):
    _name="sh.res.partner"
    _description="table for manage partner data"
    
    name=fields.Char()
    city=fields.Char()