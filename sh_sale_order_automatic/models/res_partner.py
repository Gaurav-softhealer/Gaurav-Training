from odoo import models,fields,api,Command

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    sale_workflow = fields.Many2one('sh.auto.sale.workflow',default=False)