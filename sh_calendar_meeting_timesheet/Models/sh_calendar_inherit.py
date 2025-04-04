from odoo import fields,models,api
  
class ShCalendar(models.Model):
    _inherit = "calendar.event"

    project_id = fields.Many2one('project.project')
    task_id = fields.Many2one('project.task')
    
    flag=fields.Boolean()
    reason_update=fields.Char(string="Reason for update Time")

    timesheet_ids = fields.One2many('account.analytic.line', 'calendar_id')

    @api.onchange('start')
    def reason_update_method(self):
        if self.create_date:
            self.flag=True

    @api.model_create_multi
    def create(self, val_list):
        records = super(ShCalendar, self).create(val_list)
        for record in records:
            for i in record.partner_ids:
                vals = {
                    'name': record.name, 
                    'date': record.start,
                    'project_id': record.project_id.id,
                    'task_id': record.task_id.id,
                    'unit_amount': record.duration,
                    'partner_id':i.id,
                    'calendar_id': record.id,
                }

                self.env['account.analytic.line'].create(vals)
        # ans=self.env['calendar_attendee'].search('event_id','=',self.id)
        # ans.do_accept()
        return records
    

    def write(self, val_list):
        
        # self.flag=False
        # print(f"\n\n\n\t--------------> 33 val_list",val_list)
        # print(f"\n\n\n\t--------------> 41 ",val_list['partner_ids'])
        if val_list:
                # ans=self.env['account.analytic.line'].search([('calendar_id','=',self.id)])
                # print(f"\n\n\n\t--------------> 52 ans",ans)
                # for j in ans:
                    if 'name' in val_list:
                        self.mapped('timesheet_ids').name=val_list['name']
                    if 'start' in val_list:
                        self.mapped('timesheet_ids').date=val_list['start']
                        # self.flag=True
                    if 'project_id' in val_list:
                        self.mapped('timesheet_ids').project_id=val_list['project_id']
                    if 'task_id' in val_list:
                        self.mapped('timesheet_ids').task_id=val_list['task_id']
                    if 'duration' in val_list:
                        self.mapped('timesheet_ids').unit_amount=val_list['duration']
                    if 'reason_update' in val_list:
                        self.mapped('timesheet_ids').reason_updated=val_list['reason_update']
                    if 'partner_ids' in val_list:
                        for k in val_list['partner_ids']:
                            print(f"\n\n\n\t--------------> 58 k",k)
                            if k[0]==4:
                                vals = {
                                    'name': self.name, 
                                    'date': self.start,
                                    'project_id': self.project_id.id,
                                    'task_id': self.task_id.id,
                                    'unit_amount': self.duration,
                                    'partner_id':k[1],
                                    'calendar_id': self.id,
                                }
                                self.env['account.analytic.line'].create(vals)
                            #    self.mapped('timesheet_ids').attendees_ids=[(0,0,k[1])]
                            else:
                                abc=self.env['account.analytic.line'].search([('name','=',self.name),('partner_id','=',k[1])])
                                print(f"\n\n\n\t--------------> 73 abc",abc)
                                abc.unlink()
                    # vals = {
                    #             'name': val_list['name'] , 
                    #             'date': val_list['start'] ,
                    #             'project_id': val_list['project_id'],
                    #             'task_id': val_list['task_id'],
                    #             'unit_amount': val_list['duration'],

                    #         }

                    # j.write(val_list)

        records = super(ShCalendar, self).write(val_list)
        return records

    
    
class ShTimesheet(models.Model):
    _inherit="account.analytic.line"
    
    calendar_id=fields.Many2one('calendar.event')
    attendees_ids=fields.Many2one('res.partner')
    reason_updated=fields.Char()
    
class ShCalendarAttenddees(models.Model):
    _inherit="calendar.attendee"
    
    def do_accept(self):
        print(f"\n\n\n\t--------------> 95 ","method called")
        # self.event_id.create(val_list=)
        return super().do_accept()










# from odoo import fields,models,api
  
# class ShCalendar(models.Model):
#     _inherit = "calendar.event"

#     project_id = fields.Many2one('project.project')
#     task_id = fields.Many2one('project.task')
    
#     flag=fields.Boolean()
#     reason_update=fields.Char(string="Reason for update Time")

#     timesheet_ids = fields.One2many('account.analytic.line', 'calendar_id')

#     @api.onchange('start')
#     def reason_update_method(self):
#         if self.create_date:
#             self.flag=True

#     @api.model_create_multi
#     def create(self, val_list):
#         records = super(ShCalendar, self).create(val_list)
#         for record in records:
#             for i in record.partner_ids:
#                 vals = {
#                     'name': record.name, 
#                     'date': record.start,
#                     'project_id': record.project_id.id,
#                     'task_id': record.task_id.id,
#                     'unit_amount': record.duration,
#                     'attendees_ids':i.id,
#                     'calendar_id': record.id,
#                 }

#                 self.env['account.analytic.line'].create(vals)
#         # ans=self.env['calendar_attendee'].search('event_id','=',self.id)
#         # ans.do_accept()
#         return records
    

#     def write(self, val_list):
        
#         # self.flag=False
#         # print(f"\n\n\n\t--------------> 33 val_list",val_list)
#         # print(f"\n\n\n\t--------------> 41 ",val_list['partner_ids'])
#         if val_list:
#                 # ans=self.env['account.analytic.line'].search([('calendar_id','=',self.id)])
#                 # print(f"\n\n\n\t--------------> 52 ans",ans)
#                 # for j in ans:
#                     if 'name' in val_list:
#                         self.mapped('timesheet_ids').name=val_list['name']
#                     if 'start' in val_list:
#                         self.mapped('timesheet_ids').date=val_list['start']
#                         # self.flag=True
#                     if 'project_id' in val_list:
#                         self.mapped('timesheet_ids').project_id=val_list['project_id']
#                     if 'task_id' in val_list:
#                         self.mapped('timesheet_ids').task_id=val_list['task_id']
#                     if 'duration' in val_list:
#                         self.mapped('timesheet_ids').unit_amount=val_list['duration']
#                     if 'reason_update' in val_list:
#                         self.mapped('timesheet_ids').reason_updated=val_list['reason_update']
#                     if 'partner_ids' in val_list:
#                         for k in val_list['partner_ids']:
#                             print(f"\n\n\n\t--------------> 58 k",k)
#                             if k[0]==4:
#                                 vals = {
#                                     'name': self.name, 
#                                     'date': self.start,
#                                     'project_id': self.project_id.id,
#                                     'task_id': self.task_id.id,
#                                     'unit_amount': self.duration,
#                                     'attendees_ids':k[1],
#                                     'calendar_id': self.id,
#                                 }
#                                 self.env['account.analytic.line'].create(vals)
#                             #    self.mapped('timesheet_ids').attendees_ids=[(0,0,k[1])]
#                             else:
#                                 abc=self.env['account.analytic.line'].search([('name','=',self.name),('attendees_ids','=',k[1])])
#                                 print(f"\n\n\n\t--------------> 73 abc",abc)
#                                 abc.unlink()
#                     # vals = {
#                     #             'name': val_list['name'] , 
#                     #             'date': val_list['start'] ,
#                     #             'project_id': val_list['project_id'],
#                     #             'task_id': val_list['task_id'],
#                     #             'unit_amount': val_list['duration'],

#                     #         }

#                     # j.write(val_list)

#         records = super(ShCalendar, self).write(val_list)
#         return records

    
    
# class ShTimesheet(models.Model):
#     _inherit="account.analytic.line"
    
#     calendar_id=fields.Many2one('calendar.event')
#     attendees_ids=fields.Many2one('res.partner')
#     reason_updated=fields.Char()
    
# class ShCalendarAttenddees(models.Model):
#     _inherit="calendar.attendee"
    
#     def do_accept(self):
#         print(f"\n\n\n\t--------------> 95 ","method called")
#         # self.event_id.create(val_list=)
#         return super().do_accept()