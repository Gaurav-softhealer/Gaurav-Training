from odoo import api,models,fields

class Task(models.Model):
    _name="sh.task"
    _description="this table is used to store detail about user"
    
    user_id=fields.Many2one('res.users')
    
    name=fields.Char(string="employee name")
    answer=fields.Char(string="tz field")
    
    @api.onchange('user_id')
    def _emp_data(self):
        self.name=self.user_id.name