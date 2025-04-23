from odoo import fields,models,api

class PharmacyDoctor(models.Model):
    _inherit="res.partner"
    
    is_patient=fields.Boolean()
    sh_aadhar_no=fields.Char(string="Aadhar card no")
    sh_date_of_birth=fields.Date(string="Date of Birth")
    sh_age=fields.Integer(string="Age")
    sh_allergies_ids=fields.Many2many('sh.allergy',string="Allergies")
    sh_blood=fields.Selection([
        ('A+', 'A Positive'),
        ('A-', 'A Negative'),
        ('B+', 'B Positive'),
        ('B-', 'B Negative'),
        ('O+', 'O Positive'),
        ('O-', 'O Negative'),
        ('AB+', 'AB Positive'),
        ('AB-', 'AB Negative')
    ],string="Blood group")