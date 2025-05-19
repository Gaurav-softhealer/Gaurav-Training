from odoo import http
from odoo.http import request

class WebFormController(http.Controller):

    @http.route(['/webform'], type="http", auth="public", website=True)
    def web_form(self, **kwargs):
        partners=request.env['res.partner'].sudo().search([])
        if request.session.get('name'):
            return request.render("sh_custom_web_form.web_form_template",{'partners':partners,'session':request.session.get('name   ')})
        else:
            return request.redirect('/login')

    @http.route('/webform/submit', type='http', auth='public', website=True, methods=['POST'])
    def web_form_submit(self, **post):
        
        request.env['res.partner'].sudo().create({
                    'name': post.get('name'),
                    'phone': post.get('phone'),
                    'email': post.get('email'),
                })
        return request.redirect('/thank_you')
    
    @http.route(['/thank_you'], type="http", auth="public", website=True)
    def thank_you(self, **kwargs):
        return request.render("sh_custom_web_form.thank_you_template")
    
    @http.route(['/delete/<int:id>'], type="http", auth="public", website=True)
    def delete(self, id, **kwargs):
        print(f"\n\n\n\t--------------> 31 id",id)
        partner = request.env['res.partner'].sudo().browse(id)
        if partner:
            partner.unlink()
        return request.redirect('/webform')

    @http.route(['/update/<int:id>'], type="http", auth="public", website=True)
    def updatedata(self, id, **kwargs):
        print(f"\n\n\n\t--------------> 36 updatedata",id)
        partner_data=request.env['res.partner'].search([('id','=',id)])
        return request.render("sh_custom_web_form.web_update_form_template",{'myid':id,'partner':partner_data})
    
    @http.route(['/update'], type="http", auth="public", website=True)
    def update(self,**post):
        print(f"\n\n\n\t--------------> 36 update",post.get('myid'))
        
        answer=request.env['res.partner'].search([('id','=',post.get('myid'))])
        print(f"\n\n\n\t--------------> 44 answer",answer)
        answer.sudo().write({
                    'name': post.get('name'),
                    'phone': post.get('phone'),
                    'email': post.get('email'),
                })
        return request.redirect('/webform')
    