from odoo import fields,models,api

class ProductProduct(models.Model):
    _inherit="product.product"
    
    quality_level=fields.Integer(string="Quality Level")
    