from odoo import fields,models,api

class Student(models.Model):
    _name="music.student"
    _description="this model is used to store information about the music student"
    
    name=fields.Char(required=True)
    photo=fields.Binary()
    gender=fields.Selection([
        ('male','Male'),
        ('female','Female')
    ])
    language=fields.Many2one('res.lang',string='Language')
    
    birthday=fields.Date()
    
    visa=fields.Integer(string="visa info")
    blood_group=fields.Selection([
        ('a','A+'),
        ('b','B+'),
        ('o','O+')
    ])
    
    address=fields.Char()
    mobile=fields.Integer()
    email=fields.Char()