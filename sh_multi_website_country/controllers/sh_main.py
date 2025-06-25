# from odoo import http
# from odoo.http import request

# class CountrySelector(http.Controller):

#     @http.route(['/shop1'], type='http', auth='public', website=True)
#     def country_modal(self):
#         print(f"\n\n\n\t--------------> 8 hello")
#         countries = request.env['res.country'].sudo().search([])
#         selected_id = int(request.session.get('selected_country_id', 0))
#         selected_country = request.env['res.country'].sudo().browse(selected_id)
#         return request.render("sh_multi_website_country.country_selection_modal", {
#             'country_list': countries,
#             'selected_id': selected_id,
#             'selected_country_name': selected_country.name or '',
#             'selected_country_flag': selected_country.image_url or '',
#             'country_form_action': "/country/set"
#         })

#     @http.route(['/country/set'], type='http', auth='public', methods=['POST'], csrf=False)
#     def set_country(self, **post):
#         country_id = int(post.get("country_id", 0))
#         request.session['selected_country_id'] = country_id

#         return request.redirect("/")



# # controllers/main.py
from odoo import http
from odoo.http import request

class CountryWizardController(http.Controller):

    @http.route('/country', type='http', auth='user', website=True)
    # @http.route(['/shop/<model("product.template"):product>'], type='http', auth="public", website=True, readonly=True)
    def product(self):
        action = request.env.ref('sh_multi_website_country.action_country_selection_wizard')
        return request.redirect(f"/web#action={action.id}&model=sh.country.selection.wizard&view_type=form")






# # controllers/country_popup.py
# from odoo import http
# from odoo.http import request

# class CountryPopup(http.Controller):

#     @http.route('/show/country/modal', type='http', auth='public', website=True)
#     def show_modal(self, **kwargs):
#         print(f"\n\n\n\t--------------> 54 hiiiii",)
#         countries = request.env['res.country'].sudo().search([])
#         return request.render("sh_multi_website_country.template_country_modal", {
#             'countries': countries,
#         })

