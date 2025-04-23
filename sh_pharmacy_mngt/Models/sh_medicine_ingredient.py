from odoo import fields,models

class AllergyType(models.Model):
    _name="sh.medicine.ingredient"
    _description="this model is used to store medicine ingredient"
    
    name=fields.Char(string="Ingredient Name")