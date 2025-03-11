from odoo import fields,models,api

class Equipment(models.Model):
    _name="music.equipment"
    _description="This model is used to store information about the music equipment"
    
    name=fields.Char()
    used_by=fields.Selection([
        ('department','Department'),
        ('employee','Employee'),
        ('other','Other')
    ])
    
    
