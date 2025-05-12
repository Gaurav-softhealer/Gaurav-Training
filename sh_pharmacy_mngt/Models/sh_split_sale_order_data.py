from odoo import fields,models,api

class SplitOrderData(models.Model):
    _name="sh.split.sale.order.data"
    _description="this table used for split order data"
    
    sh_split_id=fields.Many2one('sh.split.sale.order')
    product_id=fields.Many2one('product.product')
    product_qty=fields.Float()
    product_uom=fields.Many2one('uom.uom')
    price_unit=fields.Float()
    lot_ids=fields.Many2many('stock.lot')
   