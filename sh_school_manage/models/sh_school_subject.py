from odoo import fields,models,api
from datetime import datetime

class Subject(models.Model):
    _name="sh.school.subject"
    _description="sh school subject management"
    
    name=fields.Char()
    sem_id=fields.Many2one('sh.school.semester',string="semester")
