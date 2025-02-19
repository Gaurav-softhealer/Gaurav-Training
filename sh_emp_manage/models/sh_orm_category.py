from odoo import fields,models,api
import random

class Category(models.Model):
    _name="sh.orm.category"
    _description="this table is used to store data of orm category"
    
    name=fields.Char()
    ref=fields.Char()
    emp_ids=fields.Many2many('sh.orm.employee')