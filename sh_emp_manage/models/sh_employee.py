from odoo import fields,models,api

from odoo.addons.base.models.res_partner import _tz_get


class Employee(models.Model):
    _name="sh.employee"
    _description="sh employee management"

    # file = fields.Binary(attachment=True, store=True, required=True)
    # file_name=fields.Char()
    
    name=fields.Char("Full Name",required=True)
    file = fields.Binary()
    # employee_id=fields.Integer("Employee Id",required=True)
    # employee_type=fields.Selection([
    #     ('developer','Developer'),
    #     ('functional','functional'),
    #     ('hr','HR')
    # ])
    # start_date=fields.Date("Start Date")
    # address=fields.Char("Address")
    # dob=fields.Date("Birth Date")
    # working_type=fields.Selection(string="Working Type",selection=[
    #     ('full_time','Full Time'),
    #     ('part_time','Part Time'),
    #     ('intern','Intern')
    # ])
    
    # gender = fields.Selection([
    #     ('male', 'Male'),
    #     ('female', 'Female'),
    #     ('other', 'Other')
    # ])
    
    # department=fields.Char("Department")
    # shift=fields.Selection([
    #     ('night','Night Shuft'),
    #     ('day','Day Shift')
    # ])
    
   
    
    # marital_status=fields.Selection([
    #     ('married','Married'),
    #     ('unmarried','Unmarried')
    # ])
    
    # age=fields.Integer("Age")
    # aadhar_no=fields.Char("Aadhar No")
    # pan_no=fields.Char("Pan No")
    # blood=fields.Selection(string="blood group",selection=[
    #     ('a_pos','A+'),
    #     ('a_neg','A+'),
    #     ('b_pos','B+'),
    #     ('b_neg','A-'),
    #     ('ab_pos','AB+'),
    #     ('ab_neg','AB+'),
    #     ('o_pos','O+'),
    #     ('o_neg','O-')
    # ])
    
    
    # street=fields.Char()
    # street2=fields.Char()
    # city=fields.Char()
    
    # bank_name=fields.Char("Bank Name")
    # branch=fields.Char("Branch Name")
    # account_holder=fields.Char("Account Holder")
    # ifsc=fields.Char("IFSC Code")
    # account_no=fields.Char("Account No")
    
    
    
    # aadhar_doc=fields.Binary(attachment=True, store=True)
    # doc_name1=fields.Char()
    # pan_doc=fields.Binary(attachment=True, store=True)
    # doc_name2=fields.Char()
    
    
    # onoff=fields.Boolean()
    
    
    # logo=fields.Binary()
    
    # tags=fields.Char("tags")
    
    # tags2=fields.Many2many('res.partner',"tags")
    
    
    
    job_id=fields.Many2one('sh.job',string="job positions")
    # dep_id=fields.Many2one('sh.department',string="department data")
    
    state=fields.Many2one('res.country.state')
    country=fields.Many2one(related='state.country_id')
    
    
    user_id=fields.Many2one('res.users',string="user data")
    
    cat_ids=fields.Many2many('sh.emp.cat',string="category data")
    
    dep_id=fields.Many2one(related="job_id.dep_id") 
    
    tz=fields.Char(string="User Timezone")
    usr_tz=fields.Selection(_tz_get,string="Timezone")
    
    # user_tz=fields.Selection(selection=lambda self: self._get_timezones(), string="User Timezone")
    
    
    @api.onchange('user_id')
    def _change_tz(self):
        # if self.user_id:
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        self.usr_tz=self.user_id.tz
        
        
    salary=fields.Integer()
    
    
    
    
    # total_price=fields.Float(compute="_calculate_price")
    # amount=fields.Float()
    
    # @api.depends('amount')
    # def _calculate_price(self):
    #     for record in self:
    #         record.total_price=2.0*record.amount    
    