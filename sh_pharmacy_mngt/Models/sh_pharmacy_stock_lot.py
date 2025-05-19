from odoo import fields,models,api

class ShStockLot(models.Model):
    _inherit = 'stock.lot'

    @api.depends('name')
    def _compute_display_name(self):
        for template in self:
            template.display_name = False if not template.name else (
                '{}{}'.format(
                     template.name ,'[%s] ' % template.expiration_date if template.expiration_date else ''
                ))
    
