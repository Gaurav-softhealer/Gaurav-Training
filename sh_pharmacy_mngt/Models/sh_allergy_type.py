from odoo import fields,models

class AllergyType(models.Model):
    _name="sh.allergy.type"
    _description="this model is used to store allergy type"
    
    name=fields.Char(string="Allergies Type")