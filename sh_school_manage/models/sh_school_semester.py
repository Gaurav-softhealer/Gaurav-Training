from odoo import fields,models,api
from datetime import datetime

class Semester(models.Model):
    _name="sh.school.semester"
    _description="sh school semester management"
    
    name=fields.Char()
    sub_ids=fields.One2many('sh.school.subject','sem_id',string='subjects')
