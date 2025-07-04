from odoo import models, fields, api

class product_template(models.Model):
    _inherit='product.template'

    list_price = fields.Float(
        'Sales Price', default=0.0,
        digits='Product Price',
        help="Price at which the product is sold to customers.")

class Product(models.Model):
    _inherit = 'product.product'
    
    lst_price = fields.Float(
        'Sales Price', default=0.0,
        digits='Product Price',
        help="Price at which the product is sold to customers.")