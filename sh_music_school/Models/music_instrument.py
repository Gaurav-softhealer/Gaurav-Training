from odoo import fields,models,api

class Instrument(models.Model):
    _name="music.instrument"
    _description="This model is used to store information about the music instrument"
    
    name=fields.Char()