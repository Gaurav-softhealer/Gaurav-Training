from odoo import fields, models, api
from datetime import datetime,timedelta
from odoo.exceptions import UserError, ValidationError


class Classes(models.Model):
    _name = "music.classes"
    _description = "This model is used to store data about the music classes"

    name = fields.Char()

    date_from = fields.Date()
    date_to = fields.Date()

    lesson_id = fields.Many2one('music.lesson')
    lesson_duration = fields.Float(compute="_compute_lesson_duration", store=True)
    class_teacher=fields.Many2one('music.teacher',compute="_compute_lesson_duration",store=True)
    service_id=fields.Many2one('music.service',compute="_compute_lesson_duration",store=True)
    available_space=fields.Integer(compute="_compute_lesson_duration",store=True)
    student_ids=fields.Many2many('music.student')
    repeats=fields.Selection([
        ('daily','Daily'),
        ('weekly','Weelky')
    ])
    
    temp=fields.Integer(compute="_find_lesson_time")
    
    classes_lesson_line_ids=fields.One2many('music.classes.lesson.line','classes_id')

    @api.depends('lesson_id')
    def _compute_lesson_duration(self):
        for record in self:
            if record.lesson_id:
                record.lesson_duration = record.lesson_id.lesson_duration
                record.class_teacher=record.lesson_id.teacher_id
                record.service_id=record.lesson_id.service_id
                record.available_space=record.lesson_id.available_space
                record.student_ids=record.lesson_id.student_ids
            else:
                record.lesson_duration = 0.0
                record.class_teacher=False
                record.service_id=False
                record.available_space=0
                record.student_ids=False

    @api.depends('repeats')
    def _find_lesson_time(self):
        for record in self:
            if record.repeats:
                    date_format = "%Y-%m-%d"
                    # print("@@@@@@@@@@@@",str(record.date_from))
                    
                    a = datetime.strptime(str(record.date_from), date_format)
                    b = datetime.strptime(str(record.date_to), date_format)
                    
                    delta = b - a
                    
                    if record.repeats=='daily':
                        # print("--------------->",record.date_from)
                        # for i in range(3):

                        # print("###################",delta.days)
                        # print(record.date_from+timedelta(days=5))
                        for i in range(delta.days+1,):
                            print(record.date_from+timedelta(days=i))
                        record.temp=10
                        
                    
                    else:
                        for i in range(0,delta.days+1,7):
                            print(record.date_from+timedelta(days=i))
                        record.temp=20
            else:
                record.temp=0


    