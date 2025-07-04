from odoo import fields,models,api

class ShSetttingConfiguration(models.TransientModel):
    _inherit="res.config.settings"
    
    sh_multi_redirect=fields.Boolean(string="Is multiwebsite Redirect",related="company_id.sh_multi_redirect", readonly=False)
    sh_country_group_ids=fields.Many2many('res.country.group',string="country Group", related="company_id.sh_country_group_ids", readonly=False)
    
class ShCompany(models.Model):
    _inherit = 'res.company'

    sh_multi_redirect = fields.Boolean(string="Country Groups")
    sh_country_group_ids = fields.Many2many('res.country.group', string="Country Groups")