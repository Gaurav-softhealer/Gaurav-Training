from odoo import fields,models,api

class ShStockMove(models.Model):
    _inherit='stock.move'
    
    sh_partner_id=fields.Many2one('res.partner',string="Partner")
    sh_sale_document=fields.Char(string="Sale Document")
    sh_purchase_document=fields.Char(string="Purchase Document")
    