from odoo import fields,models,api

class Order(models.Model):
    _name="sh.sale.order"
    _description="this table is store data about order"
    
    name=fields.Char()
    date=fields.Date()
    
    customer_id=fields.Many2one('sh.res.partner')
    
    order_line_ids=fields.One2many('sh.sale.order.line','order_id',string="order line data")
    
    total_amount=fields.Integer(compute="_calculate_total_price")
    total_tax=fields.Integer(compute="_calculate_total_tax")
    
    @api.depends('order_line_ids')
    def _calculate_total_price(self):
        for record in self:
            total_amount=0
            print("\n\n\n\n\n\n-------------->>>>>>",record.order_line_ids)
            for i in record.order_line_ids:
                print("\n\n\n\n\n________________________>",i)
                total_amount+=i.total
            record.total_amount=total_amount
                
    @api.depends('order_line_ids')
    def _calculate_total_tax(self):
        for record in self:
            
            total_tax=0
            for i in record.order_line_ids:
                print("\n\n\n\n\n\n********&&&&&&&&&&&&&&&>>>>>>>>>",i.tax_ids)
                for j in i.tax_ids:
                    print("\n\n\n\n\n\n********************>>>>>>>>>",j)
                    total_tax+=j.tax
            record.total_tax=total_tax
    