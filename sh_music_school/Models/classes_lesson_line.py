from odoo import fields,models,api

class Classes_lesson_line(models.Model):
    _name="music.classes.lesson.line"
    _description="this model is used to store lines of classes lesson"
    _rec_name="lesson_id"
    # name=fields.Char()
    classes_id=fields.Many2one('music.classes')
    
    lesson_id=fields.Many2one('music.lesson')
    start_time=fields.Date()
    end_time=fields.Date()