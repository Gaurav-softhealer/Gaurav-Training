from odoo import fields,models

class Calendar(models.Model):
    _name="sh.calendar"
    _description="manage the all activity"
    
    name=fields.Char("Enter Activity")
    status=fields.Boolean()