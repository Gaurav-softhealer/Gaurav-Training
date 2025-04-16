from odoo import fields,models,api

class SaleConfig(models.TransientModel):
    _inherit="res.config.settings"
    
    restricted_days=fields.Integer(related='company_id.restricted_days',readonly=False)

class ResCompany(models.Model):
    _inherit="res.company"
    
    restricted_days=fields.Integer()
    
   

