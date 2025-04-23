from odoo import fields,models

class MedicineForm(models.Model):
    _name="sh.medicine.form"
    _description="this model is used to store medicine form data"
    
    name=fields.Char(string="Name")
    