from odoo import fields,models,api

class SaleConfig(models.TransientModel):
    _inherit="res.config.settings"
    
    data=fields.Boolean()
    sh_default_workflow=fields.Many2one('sh.sale.auto.workflow',related='company_id.sh_default_workflow',readonly=False,string='Work Flow')
    

class ResCompany(models.Model):
    _inherit="res.company"
    sh_default_workflow=fields.Many2one('sh.sale.auto.workflow',string='Work Flow')
    
class ResPartner(models.Model):
    _inherit="res.partner"
    
    workflow_id=fields.Many2one('sh.sale.auto.workflow')