# from odoo import fields, models, api
# import json

# class UserQuotationTemplate(models.Model):
#     _inherit = 'sale.order.template'
   
#     partner_ids = fields.Many2many('res.partner')

# class SaleOrder(models.Model):
#     _inherit = "sale.order"
    
#     @api.depends('partner_id')
#     def compute_quotation_template_domain(self):
#         for record in self:
#             if record.partner_id:
#                 templates = self.env['sale.order.template'].search([('partner_ids', 'in', record.partner_id.id)])
#                 record.quotation_template_domain = json.dumps([('id', 'in', templates.ids)])
#             else:
#                 record.quotation_template_domain = json.dumps([])  # Empty domain if no partner_id
        
#     quotation_template_domain = fields.Char(compute="compute_quotation_template_domain",store=True)



from odoo import fields, models, api

class UserQuotationTemplate(models.Model):
    _inherit = 'sale.order.template'
   
    partner_ids = fields.Many2many('res.partner')

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    @api.depends('partner_id')
    def compute_quotation_template_domain(self):
        for record in self:
            if record.partner_id:
                templates = self.env['sale.order.template'].search([('partner_ids', 'in', record.partner_id.id)])
                domain = [('id', 'in', templates.ids)]
            else:
                domain = []

            record.quotation_template_domain = str(domain)

    quotation_template_domain = fields.Char(compute="compute_quotation_template_domain")
