from odoo import fields,models,api

class PharmacyDoctor(models.Model):
    _inherit="res.partner"
    
    # company_type=fields.Selection(
    #     selection_add=[('person', 'Patient'),('doctor', 'Doctor')],
    # )
    
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
    
    
    # @api.onchange('company_type')
    # def check_doctor_patient(self):
    #     if self.company_type=='doctor':
    #         self.is_doctor=True
    #     elif self.company_type=='person':
    #         self.is_doctor=False
    
    # def _write_company_type(self):
    #     for partner in self:
    #         partner.is_company = partner.company_type == 'company'
    #         partner.is_doctor=partner.company_type=='doctor'

            
    # @api.depends('is_company')
    # def _compute_company_type(self):
    #     for partner in self:
    #         if partner.is_company:
    #             partner.company_type = 'company'
    #         elif partner.is_doctor:
    #             partner.company_type='doctor'
    #         else:
    #             partner.company_type='person'
            

    

