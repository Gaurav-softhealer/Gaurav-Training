from odoo import models,fields

class Tag(models.Model):
    _name="sh.tag"
    _description="this model is used to store information about the tags"
    
    name=fields.Char()