from odoo import http
from odoo.http import request

from odoo.http import request
import json

class CountrySelectionController(http.Controller):

    @http.route('/set_country', type="http", auth="public", methods=['POST'], website=True, csrf=False)
    def set_country(self, **kwargs):
        print("\n\n[DEBUG] kwargs:", kwargs)
        country_id = kwargs.get('country_id')
        print("\n\n[DEBUG] Received country_id:", country_id)

        # if not country_id:
        #     return request.make_response(json.dumps({
        #         'success': False,
        #         'error': 'Missing country_id'
        #     }), headers=[('Content-Type', 'application/json')])

        # try:
        country_id = int(country_id)

        country_group = request.env['res.country.group'].sudo().search([
            ('country_ids', 'in', country_id)
        ], limit=1)

        print(f"[DEBUG] Found country_group: {country_group.name if country_group else 'None'}")

        pricelist = False
        if country_group:
            pricelist = request.env['product.pricelist'].sudo().search([
                ('sh_country_group_id', '=', country_group.id),
                ('website_id','=',country_group.sh_website_id.id)
            ], limit=1)

        print(f"\n\n\n\t--------------> 78 pricelist.name",pricelist.name)
        if pricelist:
            request.session['website_sale_current_pl'] = pricelist.id
            request.session['currency'] = pricelist.currency_id.id
            request.session['selected_country_id'] = country_id

            order = request.website.sale_get_order(force_create=False)
            if order:
                order.pricelist_id = pricelist

        return request.make_response(json.dumps({
            'success': True,
        }), headers=[('Content-Type', 'application/json')])

        # except Exception as e:
        #     print("[ERROR] Exception in set_country:", str(e))
        #     return request.make_response(json.dumps({
        #         'success': False,
        #         'error': str(e)
        #     }), headers=[('Content-Type', 'application/json')])
