from odoo import fields,models,api


class ShDoctorWiseReport(models.TransientModel):
    _inherit = 'sh.report.wizard'

    is_doctor_wise = fields.Boolean()
    doctor_id = fields.Many2one('res.partner',
    domain=[('is_doctor','=',True)]
    )


    def load_data(self):
        if self.is_doctor_wise:
            if self.doctor_id:
                sale_order_rec = self.env['sale.order'].search([('sh_doctor_id.id','=',self.doctor_id.id),('date_order','>',self.start),('date_order','<',self.stop)])
                
            else:
                sale_order_rec = self.env['sale.order'].search([('date_order','>',self.start),('date_order','<',self.stop)])
            
            return super().load_data(record_ids=sale_order_rec.ids)
        else:
            return super().load_data(record_ids=[])

        
    
 