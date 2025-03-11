from odoo import fields,models,api

class Employee(models.Model):
    _name="sh.timesheet.employee"
    _description="this table is used to manage about the timesheet employee"
    
    name=fields.Char()
    hours=fields.Float()

# sh_timesheet_manage.access_sh_timesheet_employee,access_sh_timesheet_employee,sh_timesheet_manage.model_sh_timesheet_employee,base.group_user,1,1,1,1
