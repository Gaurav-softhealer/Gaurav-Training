from odoo import fields,models,api

class PharmacyDoctor(models.Model):
    _inherit="res.partner"
    
    is_vendor=fields.Boolean()
    # company_type = fields.Selection(string='Company Type',
    #     selection=[('person', 'Individual'), ('company', 'Company')],
    #     compute='_compute_company_type', inverse='_write_company_type')