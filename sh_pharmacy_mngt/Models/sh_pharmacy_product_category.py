from odoo import fields,models,api

class ShProductCategory(models.Model):
    _inherit="product.category"
    
    is_medicine=fields.Boolean()
    is_narcotics=fields.Boolean()