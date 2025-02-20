from odoo import fields,models,api

class Note(models.Model):
    _name="sh.note"
    _description="This model is used to manage note about the custom sale module"
    
    name=fields.Char()