from odoo import models,fields

class Task(models.Model):
    _name="sh.task"
    _description="this model is used to store information about the tasks"
    
    name=fields.Char()
    amount=fields.Float()
    
    timesheet_id=fields.Many2one("sh.timesheet","task_ids")
