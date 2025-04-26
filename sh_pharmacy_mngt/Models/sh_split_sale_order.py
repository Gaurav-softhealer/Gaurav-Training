from odoo import fields,models,api

class ShSplitSaleOrder(models.TransientModel):
    _name="sh.split.sale.order"
    _description="this model is used to store data about split sale order"
    
    sh_product_id=fields.Many2one('product.template')