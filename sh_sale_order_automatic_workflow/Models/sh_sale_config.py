from odoo import fields,models,api

class SaleConfig(models.TransientModel):
    _inherit="res.config.settings"
    
    # data=fields.Boolean()
    sh_sale_workflow=fields.Boolean(string="sale order workflow automatic",related='company_id.sh_sale_workflow',readonly=False)
    sh_default_workflow=fields.Many2one('sh.sale.auto.workflow',related='company_id.sh_default_workflow',readonly=False,string='Work Flow')
    
    @api.model
    def set_values(self):
        super(SaleConfig, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param("sh_sale_order_automatic_workflow.sh_sale_workflow", self.sh_sale_workflow)
 
        group = self.env.ref('sh_sale_order_automatic_workflow.sh_sale_order_automatic_security_new', raise_if_not_found=False)
        if group:
            if self.sh_sale_workflow:
                group.users = [(6,0, self.env['res.users'].search([]).ids)]
            else:
                group.users = [(5,0,0)]

class ResCompany(models.Model):
    _inherit="res.company"
    sh_sale_workflow=fields.Boolean()
    sh_default_workflow=fields.Many2one('sh.sale.auto.workflow',string='Work Flow')
    
class ResPartner(models.Model):
    _inherit="res.partner"
    
    workflow_id=fields.Many2one('sh.sale.auto.workflow')