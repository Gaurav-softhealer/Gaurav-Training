from odoo import fields,models,api

class ExpiryWise(models.Model):
    _name="sh.expiry.report"
    _description="this model is used to store data about expiry date"
    
    expiry_lot_id=fields.Many2one('stock.lot')
    product_id=fields.Many2one('product.product')
    lot_id=fields.Char()
    expiration_date=fields.Datetime()
    alert_date=fields.Datetime()
    product_qty=fields.Float()
    category_id=fields.Many2one('product.category')
    remaining_days=fields.Char()