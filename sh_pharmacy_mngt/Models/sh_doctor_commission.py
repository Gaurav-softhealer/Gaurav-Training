from odoo import fields,models,api

class ShDoctorCommission(models.Model):
    _name='sh.doctor.commission'
    _description="this models is used to store information about doctor commission"
    
    date=fields.Date()
    sh_so_id=fields.Many2one('sale.order',string="Reference Number")
    patient_id=fields.Many2one('res.partner',domain=[('is_patient','=',True)])
    sh_so_amount=fields.Integer(string="Total Amount")
    commission_type=fields.Many2one('sh.commission.type')
    doctor_commission_type=fields.Char(string="Commission Type")
    commission_rate=fields.Float(string="Commission Rate (%)")
    dr_commission=fields.Integer()
    
    
    doctor_id=fields.Many2one('res.partner')
    sh_doctor_id=fields.Many2one('res.partner')
