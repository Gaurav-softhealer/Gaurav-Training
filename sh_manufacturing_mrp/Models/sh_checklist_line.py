from odoo import fields,models,api

class Sh_checklist_Line(models.Model):
    _name="sh.checklist.line"
    _description="this model is used to manage checklist line"
    
    name=fields.Many2one('sh.manufacturing.checklist')
    description=fields.Char()
    date=fields.Date(default=lambda self: self.man_order_id.date_start)
    state=fields.Selection([
        ('New','new'),
        ('Completed','completed'),
        ('Cancelled','cancelled')
    ],default='New')
    man_order_id=fields.Many2one('mrp.production')
    
    def complete_button(self):
        print(f"\n\n\n\t--------------> 15 ","complete button called")
        self.state='Completed'
        
        
    def cancle_button(self):
        print(f"\n\n\n\t--------------> 18 ","cancle button called")
        self.state='Cancelled'