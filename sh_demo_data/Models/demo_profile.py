from odoo import fields,models

class Demodata(models.Model):
    _name='demo.profile'
    _description="this model for demo data"
    
    name=fields.Char()
    age=fields.Integer()
    gender=fields.Selection([
        ('male','Male'),
        ('female','Female')
    ])
    
    image=fields.Binary()
    
    user_id=fields.Many2one('res.users')