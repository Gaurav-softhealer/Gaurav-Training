from odoo import http, fields
from odoo.http import request

class ShController(http.Controller):
    
    @http.route('/mywebsite',type='http', auth='public', website=True)
    def mywebsite_controller(self):
        print(f"\n\n\n\t--------------> 8 Hello world",)
        


        
    