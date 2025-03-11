from odoo import fields,models,api
from odoo.exceptions import UserError, ValidationError

class Lesson(models.Model):
    _name="music.lesson"
    _description="This model is used to store information about the music lesson"
    
    name=fields.Char()
    student_ids=fields.Many2many('music.student',string="students")
    
    lesson_duration=fields.Float()
    available_space=fields.Integer()
    
    teacher_id=fields.Many2one('music.teacher',string="Teacher")
    service_id=fields.Many2one('music.service',string="service")
    instrument_id=fields.Many2one('music.instrument')
    
    @api.onchange('lesson_duration')
    def _lession_duration_limit(self):
            print("****************")
            if self.lesson_duration>6.0:
                raise ValidationError("please set less time")
            
    classes_id=fields.Many2one('music.classes')