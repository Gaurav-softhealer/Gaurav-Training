from odoo import fields,models

class Allergy(models.Model):
    _name="sh.allergy"
    _description="this model is used to store allergy"
    
    name=fields.Char(string="Name")
    sh_type=fields.Many2one('sh.allergy.type',"allergies type")