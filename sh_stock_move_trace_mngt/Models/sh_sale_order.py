from odoo import fields,models,api

class ShSaleOrder(models.Model):
    _inherit='sale.order'
    
    def action_confirm(self):
        res= super().action_confirm()

        for order in self:
            print(f"\n\n\n\t--------------> 10 ",order.name)
            for picking in order.picking_ids:
                print(f"\n\n\n\t--------------> 12 ",picking.name)
                for move in picking.move_ids_without_package:
                    print(f"\n\n\n\t--------------> 14 ",move.name)
                    move.write({
                        'sh_partner_id':order.partner_id.id,
                        'sh_sale_document':order.name,
                    })
                    
                    for line in move.move_line_ids:
                        print(f"\n\n\n\t--------------> 21 ",line.reference)
            
        return res