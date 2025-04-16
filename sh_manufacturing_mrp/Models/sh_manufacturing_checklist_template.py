from odoo import fields,models,api

class Sh_Manufacturing_checklist_template(models.Model):
    _name="sh.manufacturing.checklist.template"
    _description="this model is used to manage manufacturing checklist template"
    
    name=fields.Char()
    check_list_ids=fields.Many2many('sh.manufacturing.checklist',relation="sh_checklist_template")
    company_id=fields.Many2one('res.company',default=lambda self: self.env.company)
    
    
    
    
    
    
    
        # def complete_button(self):
    #     print(f"\n\n\n\t--------------> 15 ","complete button called")
    #     if self.cancle:
    #         self.complete=False
    #     else:
    #         self.complete=True
        
        
    # def cancle_button(self):
    #     print(f"\n\n\n\t--------------> 18 ","cancle button called")
    #     if self.complete:
    #         self.cancle=False
    #     else:
    #         self.cancle=True