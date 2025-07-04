# -*- coding: utf-8 -*-

from odoo import models, fields, api
class QuotationTemplateReport(models.Model):
	_inherit = "purchase.order"

	freight_forwarder = fields.Many2one('freight.details',string = "Freight Forwarder")


class FreightDetails(models.Model):
	_name = 'freight.details'

	name = fields.Char(string = "Freight Name")
	address = fields.Text(string = "Address")
	street = fields.Char()
	street2 = fields.Char()
	city = fields.Char()
	state_id = fields.Many2one("res.country.state", string='State', help='Enter State', ondelete='restrict')
	zip_id  = fields.Char()
	country_id = fields.Many2one('res.country', string='Country', help='Select Country', ondelete='restrict')    
	phone_no = fields.Char(string = "Phone Number")

	@api.onchange('country_id')
	def _onchange_country_id(self):
		if self.country_id:
			return {'domain': {'state_id': [('country_id', '=', self.country_id.id)]}}
		else:
			return {'domain': {'state_id': []}}

	


   