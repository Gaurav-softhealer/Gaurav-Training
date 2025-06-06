from odoo import fields, models, api
from odoo.exceptions import UserError

class ShPurchase(models.Model):
    _inherit = 'purchase.order.line'

    sh_route = fields.Many2many('stock.route', string="Routes")
    sh_picking_type_id = fields.Many2one('stock.picking.type', string="Picking Type")