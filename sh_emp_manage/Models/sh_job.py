from odoo import fields,models,api

class Job(models.Model):
    _name="sh.job.new"
    _description="manage all job available in company"
    
    name=fields.Char("job position")
    
    emp_ids=fields.One2many('sh.employee.new','job_id',string='employee data')
    dep_id=fields.Many2one('sh.department.new',string="department data")
    
    job_man_id=fields.Many2one('sh.employee.new',string="manager data")
    
    fav_user_ids=fields.Many2many(
        'res.users',
        string="favorite users data",
        relation="one_fav_user_have_contain_multiple_user1",
        column1='fav_user_ids',
        column2='user_id',
        )
    
    interviewer_ids=fields.Many2many(
        'res.users',
        string="interviewer user data",
        relation="one_fav_user_have_contain_multiple_user2",
        column1='interviewer_ids',
        column2='user_id',
        )
    
    ex_interviewer_ids=fields.Many2many(
        'res.users',
        string="ex user data",
        relation="one_fav_user_have_contain_multiple_user3",
        column1='ex_interviewer_ids',
        column2='user_id',
        )
    
    
    count=fields.Integer(compute="_count_total_emp")
    
    @api.depends('emp_ids')
    def _count_total_emp(self):
        print(self)
        for record in self:
            print("\n\n\n\n\n\n",type(record.emp_ids))
            record.count=len(record.emp_ids)
            
            
