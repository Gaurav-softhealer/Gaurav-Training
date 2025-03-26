from odoo import fields,models,api

class ProductVariant(models.Model):
    _inherit="product.product"
    
    text=fields.Char()