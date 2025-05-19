from odoo import fields,models,api

class CustomWebUser(models.Model):
    _name="custom.web.form.user"
    _description="this model is used to store detail about custom web form user"
    
    name=fields.Char(string="Name")
    password=fields.Char(string="Password")

    
    
