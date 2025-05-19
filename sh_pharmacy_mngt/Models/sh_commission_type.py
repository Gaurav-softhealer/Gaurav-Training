from odoo import fields,models

class CommissionType(models.Model):
    _name="sh.commission.type"
    _description="this model is used to store commission type"
    
    name=fields.Char(string="Name")
    sh_dr_ids=fields.One2many('res.partner','commission_type_id',string="Doctors")
