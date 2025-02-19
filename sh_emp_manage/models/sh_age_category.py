from odoo import fields,models,api
import random

class Age(models.Model):
    _name="sh.age.category"
    _description="this table is used to store data of orm create"
    
    name=fields.Char()

    min_age=fields.Integer()
    max_age=fields.Integer()
    