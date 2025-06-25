from odoo import fields,models,api,http
from odoo.http import request

class ShCountryGroup(models.Model):
    _inherit="res.country.group"
    
    sh_website_id=fields.Many2one("website",string="Website")
    sh_country_group_line=fields.One2many('product.pricelist','sh_country_group_id')
    
    
class ShPricelist(models.Model):
    _inherit="product.pricelist"
    
    sh_country_group_id=fields.Many2one('res.country.group')
    
    
