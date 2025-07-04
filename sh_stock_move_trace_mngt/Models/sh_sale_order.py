from odoo import fields,models,api

class ShSaleOrder(models.Model):
    _inherit='sale.order'
    
    def action_confirm(self):
        res= super().action_confirm()

        for order in self:
            for picking in order.picking_ids:
                for move in picking.move_ids_without_package:
                    move.write({
                        'sh_partner_id':order.partner_id.id,
                        'sh_sale_document':order.name,
                    })
        return res