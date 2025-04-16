from odoo import fields,models,api

class Sh_Manufacturing_checklist(models.Model):
    _name="sh.manufacturing.checklist"
    _description="this model is used to manage manufacturing checklist"
    
    sequence=fields.Integer()
    name=fields.Char()
    description=fields.Char()
    company_id=fields.Many2one('res.company',default=lambda self: self.env.company)
    # state=fields.Selection([
    #     ('New','new'),
    #     ('Completed','completed'),
    #     ('Cancelled','cancelled')
    # ],default='New')
    # man_order_id=fields.Many2one('mrp.production')
    # date=fields.Datetime(default=lambda self: self.man_order_id.date_start)

    
    # def complete_button(self):
    #     print(f"\n\n\n\t--------------> 15 ","complete button called")
    #     self.state='Completed'
        
        
    # def cancle_button(self):
    #     print(f"\n\n\n\t--------------> 18 ","cancle button called")
    #     self.state='Cancelled'
        

  