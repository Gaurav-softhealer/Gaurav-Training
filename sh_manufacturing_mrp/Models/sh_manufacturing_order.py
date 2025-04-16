from odoo import fields,models,api

class Sh_manufacturing_order(models.Model):
    _inherit='mrp.production'
    
    # test=fields.Char()
    checklist_completed=fields.Float(default=0,compute="_checklist_complete_method",store=True)
    checklist_template_id=fields.Many2many('sh.manufacturing.checklist.template')
    checklist_line_ids=fields.One2many('sh.checklist.line','man_order_id')
    
    @api.onchange('checklist_template_id')
    def onchange_checklist(self):
        self.checklist_line_ids=[(5,0,0)]
        if self.checklist_template_id:
            for record in self.checklist_template_id:
                for i in record.check_list_ids:
                    # if i.id not in self.checklist_line_ids.ids:
                        print(f"\n\n\n\t--------------> 15 record",record)
                        vals={
                            'name':i.id,
                            'description':i.description,
                        }
                        self.checklist_line_ids=[(0,0,vals)]
                    
    # count=0 
    # total=0              
    @api.depends('checklist_line_ids.state')
    def _checklist_complete_method(self):
        for rec in self:     
        # for record in self.checklist_template_id:
        #     for i in record.check_list_ids:
        #         print(f"\n\n\n\t--------------> 29 i",i)
                print(f"\n\n\n\t--------------> 30 ","compute method called")
                count=0 
                total=0
                rec.checklist_completed=0.0 
                if self.checklist_line_ids:
                    print(f"\n\n\n\t--------------> 35 ",len(self.checklist_line_ids))
                    for record in rec.checklist_line_ids:
                        # total+=1
                        if record.state=='Completed':
                            count+=1
                    if len(rec.checklist_line_ids.ids)>0:
                        rec.checklist_completed=(count)*100/len(rec.checklist_line_ids.ids)
                # else:
                #     self.checklist_completed=0.0
                    
                    
                    
                    
                    
    #          @api.depends('checklist_page_id.state')
    # def _compute_progress(self):
    #     for rec in self:
    #         rec.progress = 0
    #         completed = 0
    #         for i in rec.checklist_page_id:
    #             if i.state == 'completed':
    #                 completed +=1
    #         if len(rec.checklist_page_id.ids) > 0:
    #             rec.progress =   (completed * 100)/len(rec.checklist_page_id.ids)           
                    
                    
                    
                    
                    
                    
                    
        # for record in self.checklist_line_ids:
        #         print(f"\n\n\n\t--------------> 29 ",len(self.checklist_line_ids.checklis))
        #         ans=self.env['sh.checklist.line'].search([('state','=','Completed')])
        #         all=self.env['sh.checklist.line'].search([('id','=',self.id),('state','in',['Completed','New','Cancelled'])])
        #         print(f"\n\n\n\t--------------> 30 ans",len(ans))
        #         print(f"\n\n\n\t--------------> 34 ",len(all))
        #         self.checklist_completed=len(ans)
                    
        # if self.checklist_line_ids:
        #     print(f"\n\n\n\t--------------> 26 ",len(self.checklist_line_ids))
        #     # self.checklist_completed=len(self.checklist_ids)
        #     print(f"\n\n\n\t--------------> 27 ",len(self.checklist_line_ids))
            
        #     answer=self.env['sh.checklist.line'].search([('state','=','Completed')])
            
        #     print(f"\n\n\n\t--------------> 32 self.answer",len(answer))
                
                # vals={
                #     'name':record.name
                # }
                # # self.checklist_ids=[(0,0,vals)]
                # # self.checklist_ids=[4,record.id]
                # for record in self.checklist_template_id:
                #     self.checklist_line_ids=[(0,0,record.check_list_ids.ids)]
                    



















# from odoo import fields,models,api

# class Sh_manufacturing_order(models.Model):
#     _inherit='mrp.production'
    
#     # test=fields.Char()
#     checklist_completed=fields.Float()
#     checklist_template_id=fields.Many2one('sh.manufacturing.checklist.template')
#     checklist_ids=fields.One2many('sh.manufacturing.checklist','man_order_id')
    
#     @api.onchange('checklist_template_id')
#     def onchange_checklist(self):
#         if self.checklist_template_id:
#             # for record in self.checklist_template_id.check_list_ids:
#                 # vals={
#                 #     'name':record.name
#                 # }
#                 # self.checklist_ids=[(0,0,vals)]
#                 # self.checklist_ids=[4,record.id]

#                     self.checklist_ids=[(6,0,self.checklist_template_id.check_list_ids.ids)]
                    
#     # @api.onchange('checklist_ids.state')
#     # def checklist_complete(self):
#     #         # self.checklist_completed=100
#     #     # if self.checklist_ids:
#     #         print(f"\n\n\n\t--------------> 26 ",len(self.checklist_ids))
#     #         self.checklist_completed=len(self.checklist_ids)
            
#     #         answer=self.env['sh.manufacturing.checklist'].search([('state','=','Completed')])
            
#     #         print(f"\n\n\n\t--------------> 32 self.answer",len(answer))
