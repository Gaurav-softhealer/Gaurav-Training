from odoo import fields,models,api

class ShPharmacyOrderLine(models.Model):
    _inherit="sale.order.line"
    
    is_selected=fields.Boolean()
    sh_lot_no=fields.Char(string="Lot No")
    sh_expiration_date=fields.Datetime()
    split_id=fields.Many2one('sh.split.sale.order')
    lot_ids=fields.Many2many('stock.lot')