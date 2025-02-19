from odoo import fields,models

class Product(models.Model):
    _name="sh.product.product"
    _description="this table is used to store product data"
    
    name=fields.Char()