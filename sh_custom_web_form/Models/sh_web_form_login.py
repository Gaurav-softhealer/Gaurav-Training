from odoo import http
from odoo.http import request

class WebFormControllerLogin(http.Controller):
    
    @http.route(['/login'], type="http", auth="public", website=True)
    def login(self, **post):
        if request.httprequest.method=='POST':
            available=request.env['custom.web.form.user'].search([('name','=',post.get('name'))])
            print(f"\n\n\n\t--------------> 10 ",available)
            if not available:
                print(f"\n\n\n\t--------------> 11 ","User not Exist")
            else:
                access=request.env['custom.web.form.user'].search([('name','=',post.get('name')),('password','=',post.get('password'))])
                if access:
                    request.session['name']=post.get('name')
                    print(f"\n\n\n\t--------------> 17 ",request.session.get('name'))
                    partners=request.env['res.partner'].sudo().search([])
                    # return request.render('sh_custom_web_form.web_form_template',{'partners':partners,'session':request.session['name']})
                    return request.redirect('/webform')
        return request.render("sh_custom_web_form.web_form_login_template")
    
    @http.route(['/signup'], type="http", auth="public", website=True)
    def signup(self, **post):
        if request.httprequest.method=='POST':
            available=request.env['custom.web.form.user'].search([('name','=',post.get('name'))])
            if available:
                print(f"\n\n\n\t--------------> 17 ","User Already Exist!!!")
            else:
                request.env['custom.web.form.user'].create({
                    'name':post.get('name'),
                    'password':post.get('password'),
                })
                return request.redirect('/login')
        return request.render("sh_custom_web_form.web_form_signup_template")
    
    @http.route(['/logout'], type="http", auth="public", website=True)
    def logout(self, **kwargs):
        del request.session['name']
        # request.session.flush()
        return request.redirect('/login')
        
    
    