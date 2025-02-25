from odoo import fields,models

class Category(models.Model):
    _name="sh.emp.cat.new"
    _description="this table is used to manage users category"
    
    name=fields.Char("Enter category")
    
    emp_ids=fields.Many2many('sh.employee.new',string="employee data")