from odoo import fields, models, api
from odoo.exceptions import UserError

class ShPurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def button_confirm(self):
        res = super(ShPurchaseOrder, self).button_confirm()

        for order in self:
            for line in order.order_line:
                for route in line.sh_route:
                    for rule in route.rule_ids:
                        picking_type = (
                            line.sh_picking_type_id
                            or self.env['stock.picking.type'].search([
                                ('code', '=', 'incoming'),
                            ], limit=1)
                        )

                        records=self.env['stock.picking'].search([('origin','=',order.name),('purchase_id', '=', order.id),
                                ('location_id','=',rule.location_src_id.id),('location_dest_id','=',rule.location_dest_id.id)])
                        print("----------------->",records)

                        if not records:
                            picking = self.env['stock.picking'].create({
                                'partner_id': order.partner_id.id,
                                'picking_type_id': picking_type.id,
                                'location_id': rule.location_src_id.id,
                                'location_dest_id': rule.location_dest_id.id,
                                'origin': order.name,
                                'purchase_id': order.id,
                            })

                            self.env['stock.move'].create({
                                'name': line.name,
                                'product_id': line.product_id.id,
                                'product_uom_qty': line.product_qty,
                                'product_uom': line.product_uom.id,
                                'picking_id': picking.id,
                                'location_id': rule.location_src_id.id,
                                'location_dest_id': rule.location_dest_id.id,
                                'purchase_line_id': line.id,
                            })

        return res
