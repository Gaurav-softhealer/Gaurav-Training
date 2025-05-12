from odoo import fields,models,api

class PharmacyDoctor(models.Model):
    _inherit="res.partner"
    
    dr_commission_ids=fields.One2many('sh.doctor.commission','doctor_id')
    
    gender=fields.Selection([
        ('male','Male'),
        ('female','Female')
    ])
    
    is_doctor=fields.Boolean()
    
    specialization_ids=fields.Many2many('sh.specialization.category',string="Specialization")
    
    commission_type_id=fields.Many2one('sh.commission.type',string="Commission Type")
    sh_amount=fields.Monetary(string="Amount")
    currency_id = fields.Many2one('res.currency', string="Currency",
                                 related='company_id.currency_id',
                                 default=lambda
                                 self: self.env.user.company_id.currency_id.id)
    commission_percent=fields.Float(string="Commission Rate")
    
    commission_total=fields.Float(compute="cal_total_commission")
    
    doctor_commission_type=fields.Selection([
        ('by_patient','By Patient'),
        ('by_amount','By Amount'),
        
    ],string="Commission Type")
    
    @api.depends('dr_commission_ids')
    def cal_total_commission(self):
        total=0
        for record in self:
            for i in record.dr_commission_ids:
                total+=i.dr_commission
            record.commission_total=total
    
    

