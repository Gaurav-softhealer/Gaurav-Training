# from odoo import fields,models,api

# class Attendence(models.Model):
#     _name="sh.attendence"
#     _description="this model is used to manage the attendence about the employee"
    
#     name=fields.Many2one('sh.timesheet')
#     # status=fields.Selection(selection=[
#     #     ('fulltime','Fulltime'),
#     #     ('halftime','Halftime')

#     # ],compute="_find_time_attend")
    
#     time=fields.Char(compute="_find_time_attend")
    
#     @api.depends('name')
#     def _find_time_attend(self):
#         for record in self:
#             if record.name:
#                 print("##################",record.name)



from odoo import fields, models, api

class Attendence(models.Model):
    _name = "sh.attendence"
    _description = "This model is used to manage attendance about the employee"

    # name = fields.Many2one('sh.timesheet')
    
    # name=fields.Many2one('sh.timesheet')
    
    # status=fields.Selection(selection=[
    #     ('fulltime','Fulltime'),
    #     ('leave','Leave'),
    #     ('halftime','Halftime')
    # ],compute="_find_time_attend")
    
    # time = fields.Char(compute="_find_time_attend")

    # @api.depends('name')
    # def _find_time_attend(self):
    #     for record in self:
    #         if record.name:
    #             print("##################", record.name.hours)
    #             if record.name.hours>50.0:
    #                 record.status = "fulltime" 
    #             elif record.name.hours<50.0 and record.name.hours>0.0:
    #                 record.status="halftime"
    #             elif record.status==0.0:
    #                 record.status="leave"
    #         else:
    #             record.status=""
                
                
                
                
