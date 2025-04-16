# models/stock_production_lot.py
from odoo import models, fields

class StockProductionLot(models.Model):
    _inherit = 'stock.move'

    custom_reference = fields.Char(string="Custom Reference")
    is_delivery=fields.Boolean()
    
    def default_get(self, fields_list):
        print(f"\n\n\n\t--------------> 29 ","button called")
        print(f"\n\n\n\t--------------> 30 self.env.context",self.env.context)
        print(f"\n\n\n\t--------------> 31 self.env.context.get('picking_type_code')",self.env.context.get('picking_type_code'))
        rtn = super().default_get(fields_list)
        if self.env.context.get('picking_type_code') == 'outgoing':
            # self.is_delivery=True
            rtn.update({'is_delivery': True})
        # else:
        #     rtn.update({'is_delivery': False})
        return rtn
    
    # action_product_forecast_report()
    
class StockMoveLineCustom(models.Model):
    _inherit="stock.move.line"
    
    test=fields.Char()
    
    is_delivery=fields.Boolean()

    def default_get(self, fields_list):
        print(f"\n\n\n\t--------------> 29 ","button called")
        print(f"\n\n\n\t--------------> 30 self.env.context",self.env.context)
        print(f"\n\n\n\t--------------> 31 self.env.context.get('picking_type_code')",self.env.context.get('picking_type_code'))
        rtn = super().default_get(fields_list)
        if self.env.context.get('picking_type_code') == 'outgoing':
            rtn.update({'is_delivery': True})
        # else:
        #     rtn.update({'is_delivery': False})
        return rtn

