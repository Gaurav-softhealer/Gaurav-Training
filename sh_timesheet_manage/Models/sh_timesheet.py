from odoo import models,fields,api
from datetime import datetime

class Timesheet(models.Model):
    _name="sh.timesheet"
    _inherit = ['mail.thread']
    _description="this model is used to store information about the timesheet"
    
    # name=fields.Many2one('sh.timesheet.employee',required=True)
    name=fields.Many2one('sh.timesheet.employee',string="Employee Name")
    
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
    
    all_ids=fields.Reference([
        ("sh.tag",'Tag'),
        ('sh.task','Task'),
        ('sh.timesheet','Timesheet')
    ])
    
    company_id=fields.Many2one('res.company')
    
    manager_id=fields.Many2one('res.users')
    
    @api.depends('task_ids')
    def _calculate_total_amount(self):
        for record in self:
            record.total_amount=len(record.task_ids)
            total_amount_all=0.0
            for i in record.task_ids:
                total_amount_all+=i.amount
            record.hours=total_amount_all
    
    
    def default_get(self,fields):
        res=super(Timesheet,self).default_get(fields)
        # res['user_id']=self.env.uid
        res['date']=datetime.today()
        res['company_id']=self.env.user.company_id
        return res
    
    def submit_manager(self):
        self.state='submitted'
        
    def approve_data(self):
        self.state='approved'
        
    def reject_data(self):
        ...
        
    def task_smart(self):
        print("############################### smart button called")
            
    # def company_check(self):
    #     print("$$$$$$$$$$$$$$$$$$$$$$$$$$$",self.env.user.company_id.name)
    
    year=fields.Integer()
    
    def check_form(self):
        print(f"\n\n\n\t--------------> 82 ",self.env.context)
        
        # year=self.env.context.get
        
        return {
            'type': 'ir.actions.act_window',
            'name': 'Name of window',
            'view_mode': 'form',
            'res_model': 'sh.task',
            'res_id':3,
           
        }
        
    def check_form2(self):
        print(f"\n\n\n\t--------------> 98 ",self.env.context)
    
    # @api.model_create_multi
    # def create(self,val_list):
    #     for record in val_list:
    #         res=super(Timesheet,self).create(val_list)
    #         # result=self.env['sh.timesheet.employee'].search([('name','=',res.name)])
    #         # print("++++++++++++++++++++++++++",result)
    #         print("***************",res.hours)
    #         vals={
    #             'hours':res.hours,
    #         }
    #         self.env['sh.timesheet.employee'].create(vals)
    #         return res   
    
    cron_count=fields.Integer()
    # def action_date(self):
    #     print(f"\n\n\n\t-------------->  ","cron called")
    #     new=self.cron_count+1
    #     self.cron_count=new
    #     print("####################",new)
        
    #     # print(f"*****************",cron_count+=1)
    #     # self.cron_count+=1
    #     # print("*******************","cron called")
        
    @api.model
    def action_date(self):
        """Updates the number_field with a new random value and updates timestamp"""
        print(f"\n\n\n\t--------------> 122 ",self)
        print(f"\n\n\n\t-------------->  ","cron called")
        records = self.search([])
        for record in self:
            new_value = record.cron_count + 1  # Increment number every execution
            record.write({
                'cron_count': new_value,
                # 'last_updated': datetime.utcnow() + timedelta(hours=5, minutes=30)  # Adjust for IST
            })
        
    def action_date2(self):
        print(f"\n\n\n\t--------------> 133 ","second cron called")
        
    def action_date3(self):
        print(f"\n\n\n\t--------------> 133 ","third cron called")