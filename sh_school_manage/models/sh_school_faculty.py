from odoo import fields,models,api
from datetime import datetime

class Faculty(models.Model):
    _name="sh.school.faculty"
    _description="sh School faculty management"
    
    name=fields.Char()
    photo=fields.Binary()
    dob=fields.Date(string="Birthdate")
    age=fields.Integer(compute="_calculate_age")
    dep_id=fields.Many2one('sh.school.department',string="Department")
    
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