from odoo import fields,models,api

class FsnReportData(models.Model):
    _name="fsn.report.data"
    _description="this models is used to store data about fsn report"
    
    product_id=fields.Many2one('product.product')
    category_id=fields.Many2one('product.category')
    stock_qty=fields.Float()
    forcast_qty=fields.Float()
    qty_sold=fields.Float()
    sale_rate=fields.Selection([
        ('slow','Slow'),
        ('fast','Fast')
    ])