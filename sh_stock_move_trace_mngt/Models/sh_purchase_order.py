from odoo import fields,models,api

class ShSaleOrder(models.Model):
    _inherit='purchase.order'
    
    def button_confirm(self):
        res= super().button_confirm()

        for order in self:
            for picking in order.picking_ids:
                for move in picking.move_ids_without_package:
                    move.write({
                        'sh_partner_id':order.partner_id.id,
                        'sh_purchase_document':order.name,
                    })
        return res