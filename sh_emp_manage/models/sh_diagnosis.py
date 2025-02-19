from odoo import fields,models,api

class Doctor(models.Model):
    _name="sh.diagnosis"
    _description="table for manage all diagnosis"
    
    name=fields.Char()
    
    patient_ids=fields.Many2many('sh.patient')
    