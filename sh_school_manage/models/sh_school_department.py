from odoo import fields,models,api,_
import random

class Department(models.Model):
    _name="sh.school.department"
    _description="sh School department management"
    
    name=fields.Char()
    dep_no=fields.Char("Reference", default=lambda self: _('New'),
       copy=False, readonly=True)
    stu_ids=fields.One2many('sh.student','dep_id',string="student data")
    sub_ids=fields.Many2many('sh.school.subject',string="subjects")
    
    @api.model_create_multi
    def create(self,val_list):
        for record in val_list:
            if record.get('dep_no', _('New')) == _('New'):
                record['dep_no'] = self.env['ir.sequence'].next_by_code('student.student')
        return super(Department,self).create(val_list)
    