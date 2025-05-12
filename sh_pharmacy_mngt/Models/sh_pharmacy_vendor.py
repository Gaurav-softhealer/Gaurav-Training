from odoo import fields,models,api

class PharmacyDoctor(models.Model):
    _inherit="res.partner"
    
    is_vendor=fields.Boolean()
