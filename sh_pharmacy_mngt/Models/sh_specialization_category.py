from odoo import fields,models

class Specialization(models.Model):
    _name="sh.specialization.category"
    _description="this model is used to store specialization category"
    
    name=fields.Char(string="Specialization Name")