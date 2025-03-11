from odoo import fields,models,api

class Teacher(models.Model):
    _name="music.teacher"
    _description="This model is used to store information about the music teacher"
    
    name=fields.Char()