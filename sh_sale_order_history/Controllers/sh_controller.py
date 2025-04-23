from odoo import http
from odoo.http import request
class PurchaseOrderController(http.Controller):
    @http.route(['/purchaseorders'], type="http", auth="user", website=True)
    def display_purchase_orders(self, **kwargs):
        # Fetch purchase order records
        purchase_orders = request.env['purchase.order'].sudo().search([])
        # Prepare data for the template
        values = {
            'records': purchase_orders
        }
        # Render the template with data
        return request.render("sh_sale_order_history.purchase_order_template", values)
    
class PurchaseOrderControllerNew(http.Controller):
    @http.route(['/purchaseorders2'], type="http", auth="user", website=True)
    def display_purchase_orders(self, **kwargs):
        # Fetch purchase order records
        # purchase_orders = request.env['purchase.order']().search([])
        # # Prepare data for the template
        # values = {
        #     'records': purchase_orders
        # }
        # Render the template with data
        return request.redirect("/purchaseorders")
