from odoo import fields,models,api
from datetime import datetime,timedelta

class Warranty(models.Model):
    _name="sh.sale.warranty"
    _description="this table is used to store information about the warranty"
    
    name=fields.Char()
    sale_order_id=fields.Many2one('sale.order','Order Id',readonly=True)
    # sale_order_ide=fields.Many2one('sale.order')
    order_date=fields.Date()
    warranty_period=fields.Integer()
    warranty_expiry_date=fields.Date(compute="_find_expiry")
    
    @api.depends('order_date')
    def _find_expiry(self):
        for record in self:
            if self.order_date:
                # if record.warranty_period:
                    
                #     record.warranty_expiry_date=record.order_date + timedelta(days=365*record.warranty_period)
                # else:
                    record.warranty_expiry_date=record.order_date + timedelta(days=record.warranty_period)
            else:
                self.order_date=0
        # print("@@@@@@@@@@@@@@@@@@@@@",self.sale_order_id.date_order)

    
    