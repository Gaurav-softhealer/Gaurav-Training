from odoo import fields,models,api

class SaleHistoryConfig(models.TransientModel):
    _inherit="res.config.settings"
    
    no_of_order=fields.Integer(string="Last No. of orders",related='company_id.sh_no_of_order',readonly=False)
    sh_sale_stage=fields.Many2many('sale.order.stage',related='company_id.sh_sale_stage',readonly=False)
    no_of_day=fields.Integer(string="No. of days",related='company_id.sh_no_of_day',readonly=False)
    group_enable_reorder=fields.Boolean(string="enable Boolean",related='company_id.sh_enable_reorder',implied_group="sh_sale_order_history.sh_sale_order_history_security",readonly=False)
    
class SaleHistoryCompany(models.Model):
    _inherit="res.company"
    
    sh_no_of_order=fields.Integer()
    sh_sale_stage=fields.Many2many('sale.order.stage')
    sh_no_of_day=fields.Integer()
    sh_enable_reorder=fields.Boolean()
    