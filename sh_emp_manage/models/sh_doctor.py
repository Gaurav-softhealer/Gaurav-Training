from odoo import fields,models,api

class Doctor(models.Model):
    _name="sh.doctor"
    _description="table for manage all doctors"
    
    name=fields.Char()
    specialization=fields.Char()
    patient_ids=fields.One2many('sh.patient','doctor_id',string="patients data")
    
    def copy(self, default=None):
        
        return super().copy(default=default)