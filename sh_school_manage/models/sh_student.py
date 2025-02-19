from odoo import fields,models,api,_
from datetime import datetime

class Student(models.Model):
    _name="sh.student"
    _description="sh school student management"
    
    name=fields.Char()
    eno=fields.Char("Reference", default=lambda self: _('New'),
       copy=False, readonly=True, tracking=True)
    photo=fields.Binary()
    dob=fields.Date(string="Birthdate")
    age=fields.Integer(compute="_calculate_age")
    dep_id=fields.Many2one('sh.school.department',string="Department")
    sem_id=fields.Many2one('sh.school.semester',string="Semester")
    
    @api.depends('dob')
    def _calculate_age(self):
        for record in self:
            if record.dob:
                now=datetime.now()
                current=int(now.strftime("%Y")) 
                dob1=int(record.dob.strftime("%Y"))
                if dob1 < current:
                    record.age=current-dob1 
                else: 
                    record.age=0     
            else:
                record.age=0 
    
               
    @api.model_create_multi
    def create(self,vals_list):
            for vals in vals_list:
                dep=self.env['sh.school.department'].browse(vals['dep_id'])
                if vals.get('eno', _('New')) == _('New'):
                    vals['eno'] = f"{dep.dep_no}{(self.env['ir.sequence'].next_by_code('student.student'))}"
            return super().create(vals_list)
       




    