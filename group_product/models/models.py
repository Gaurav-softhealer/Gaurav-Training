from odoo import Command, _, api, fields, models

from odoo.exceptions import ValidationError

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def open_wizard_from_method(self):
        if not self.attribute_line_ids:
            raise ValidationError('Please add one attribute for current product to make variant first.')
        action = self.env.ref('group_product.attribute_wizard_action').read()[0]
        return action
