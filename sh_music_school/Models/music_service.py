from odoo import fields,models,api

class Service(models.Model):
    _name="music.service"
    _description="This model is used to store information about the music service"
    
    name=fields.Char()