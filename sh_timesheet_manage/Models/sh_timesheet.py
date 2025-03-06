from odoo import models,fields,api
from datetime import datetime

class Timesheet(models.Model):
    _name="sh.timesheet"
    _inherit = ['mail.thread']
    _description="this model is used to store information about the timesheet"
    
    name=fields.Char(required=True)
    
    # def _current_user(self):
    #      return self.env.uid
        
    # user_id=fields.Many2one("res.users","User",default=_current_user)
    user_id=fields.Many2one("res.users","User")
    description=fields.Html()
    # date=fields.Date(default=datetime.today())
    date=fields.Date()

    hours=fields.Float(compute="_calculate_total_amount")
    tag_ids=fields.Many2many("sh.tag",string="tags")
    
    state=fields.Selection([
        ('draft','Draft'),
        ('submitted',"submitted"),
        ('approved','Approved'),
        ('reject','Reject')
    ],default='draft')
    
    project_id=fields.Many2one('sh.project',string="project")
    task_ids=fields.One2many("sh.task",'timesheet_id',string="Tasks")
    
    total_amount=fields.Integer(compute="_calculate_total_amount")
    rejection_reason=fields.Char(string="Reason")
    rejected_by=fields.Many2one('res.users',string="Rejected by")
    rejection_time=fields.Datetime()
    
    @api.depends('task_ids')
    def _calculate_total_amount(self):
        for record in self:
            record.total_amount=len(record.task_ids)
            total_amount_all=0.0
            for i in record.task_ids:
                total_amount_all+=i.amount
            record.hours=total_amount_all
    
    
    def default_get(self,fields):
        print("###############",self)
        print("****************",fields)
        res=super(Timesheet,self).default_get(fields)
        print("@@@@@@@@@@@@@@@@@@@@",res)
        res['user_id']=self.env.uid
        res['date']=datetime.today()
        return res
    
    def submit_manager(self):
        print("######## method called")
        self.state='submitted'
        
    def approve_data(self):
        self.state='approved'
        
    def reject_data(self):
        ...
        
    def task_smart(self):
        print("############################### smart button called")
            
    # def company_check(self):
    #     print("$$$$$$$$$$$$$$$$$$$$$$$$$$$",self.env.user.company_id.name)