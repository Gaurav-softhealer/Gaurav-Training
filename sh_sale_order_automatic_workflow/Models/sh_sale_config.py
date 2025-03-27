from odoo import fields,models,api

class SaleConfig(models.TransientModel):
    _inherit="res.config.settings"
    
    data=fields.Boolean()