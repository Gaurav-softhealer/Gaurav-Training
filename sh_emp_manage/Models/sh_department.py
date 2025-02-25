from odoo import fields,models,api

class Department(models.Model):
    _name="sh.department.new"
    _description="this model is used to manage department of the company"
    
    name=fields.Char("Enter Department")
    
    job_ids=fields.One2many('sh.job.new','dep_id',string="job data")
    # emp_ids=fields.One2many('sh.employee','dep_id',string="employee data")
    
    parent_dep_id=fields.Many2one('sh.department.new',string="parent department data")
    
    manager_id=fields.Many2one('sh.employee.new',string="manager data")
    
    
    all_salary=fields.Integer()
    
    employees=fields.One2many('sh.employee.new','dep_id',compute="_calculate_salary")
    
    total_salary=fields.Integer()
    
    @api.depends('name')
    def _calculate_salary(self):
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",self)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",type(self))
        for record in self:
            print("********************************************",self)
            # print(record.name)
            # record.all_salary=record.parent_dep_id
    
            record.employees = record.env['sh.employee.new'].search([('dep_id', '=', record.id)])
            print(record.employees)
                
            # for i in record:
            #     print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",i.employees.salary)
            #     i.all_salary=sum(i.employees.salary)
    
  
        