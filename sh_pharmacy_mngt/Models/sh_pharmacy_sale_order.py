from odoo import fields,models,api
from datetime import datetime

class ShPharmacySale(models.Model):
    _inherit="sale.order"
    
    sh_doctor_id=fields.Many2one('res.partner',domain=[('is_doctor','=',True)],string="Doctor")
    sh_prescription=fields.Binary(string="Upload Prescription")
    
    sh_mobile_no=fields.Char(string="Mobile Number")
    sh_aadhar_card=fields.Char(string="Aadhar Card Number")
    
    is_selected=fields.Boolean()
    is_narcotics=fields.Boolean()
    
    sh_customer_allergy_ids=fields.Many2many('sh.allergy',string="Customer Allergies")

    
    
    def action_confirm(self):
        if self.sh_doctor_id:
            if self.sh_doctor_id.doctor_commission_type=='by_patient':
            
            # if self.sh_doctor_id.commission_type_id.name=='By Patient':
                
                vals={
                    'date':datetime.today(),
                    'sh_so_id':self.id,
                    'patient_id':self.partner_id.id,
                    'sh_so_amount':self.amount_untaxed,
                    'doctor_commission_type':self.sh_doctor_id.doctor_commission_type,
                    'commission_rate':self.sh_doctor_id.commission_percent,
                    'dr_commission':self.sh_doctor_id.sh_amount
                    
                }
            if self.sh_doctor_id.doctor_commission_type=='by_amount':
                ans=(self.sh_doctor_id.commission_percent/100)*self.amount_untaxed
            
                vals={
                    'date':datetime.today(),
                    'sh_so_id':self.id,
                    'patient_id':self.partner_id.id,
                    'sh_so_amount':self.amount_untaxed,
                    'doctor_commission_type':self.sh_doctor_id.doctor_commission_type,
                    'commission_rate':self.sh_doctor_id.commission_percent,
                    'dr_commission':ans
                    
                }
            
            self.sh_doctor_id.dr_commission_ids=[(0,0,vals)]
        return super().action_confirm()
    

    def action_cancel(self):

        
        answer=self.env['sh.doctor.commission'].search([('sh_so_id','=',self.id)])
        print(f"\n\n\n\t--------------> 59 answer",answer)
        
        for record in answer:
            self.sh_doctor_id.dr_commission_ids=[(2,record.id)]

        return super().action_cancel()


    
    
    def split_sale_order(self):
        print(f"\n\n\n\t--------------> 13 ","Split function called")
        print(f"\n\n\n\t--------------> 69 self.order_line",self.order_line.read())

        order_lines_data = []
        for record in self.order_line:
            # if record.is_selected:
                # order_lines_data.append((0, 0, {
                #     'product_id': record.product_id.id,
                    # 'product_uom_qty': record.product_uom_qty,
                    # 'product_uom': record.product_uom.id, 
                    # 'price_unit': record.price_unit,
                    # 'name': record.name,
                    # 'tax_id': [(6, 0, record.tax_id.ids)]
                # }))
                
                order_lines_data.append(record.product_id.id)
            
        print(f"\n\n\n\t--------------> 26 order_lines_data",order_lines_data)
        print(f"\n\n\n\t--------------> 85 record.product_id.id",record.product_id.id)
        return {
                'type': 'ir.actions.act_window',
                'name': 'Split Sale Order',
                'view_mode': 'form',
                'res_model': 'sale.order',
                'target': 'new',
                'context': {
                    'default_partner_id': self.partner_id.id,
                    'default_order_line': [{'product_id':record.product_id.id,'product_uom_qty': record.product_uom_qty,
                    'product_uom': record.product_uom.id, 
                    'price_unit': record.price_unit,
       
                    }],
                #     # 'default_state': 'draft',
                #     # 'default_origin': self.name,
                }
            }
    
    
    
    

            
    


    
    
    
    
    
        
    @api.onchange('order_line')
    def check_narco(self):
        for record in self.order_line:
            print(f"\n\n\n\t--------------> 97 record.product_id.categ_id",record.product_id.categ_id.name)
            if record.product_id.categ_id.name=='Narcotics':
                self.is_narcotics=True
            else:
                self.is_narcotics=False
            
            # record.sh_lot_no=self.order_line.move_ids.order_line.lot_id.name
            
        
    @api.onchange('partner_id')
    def customer_allergies(self):
        if self.partner_id:
            self.sh_aadhar_card=self.partner_id.sh_aadhar_no
            self.sh_mobile_no=self.partner_id.phone
            self.sh_customer_allergy_ids=[(6,0,self.partner_id.sh_allergies_ids.ids)]


        
        
class ShPharmacyOrderLine(models.Model):
    _inherit="sale.order.line"
    
    is_selected=fields.Boolean()
    # data=fields.Char()
    sh_lot_no=fields.Char(string="Lot No")
    sh_expiration_date=fields.Datetime()
    # lot_id = fields.Many2one('stock.production.lot', string='Lot/Serial Number', readonly=True)
   
    @api.onchange('product_id')
    def check_lot(self):
        for record in self:
            print(f"\n\n\n\t--------------> 125 ",record.product_id.name)
            lot = self.env['stock.move.line'].search([
                    ('product_id', '=', record.product_id.id),
                   
                ],limit=1)
            print(f"\n\n\n\t--------------> 149 lot",lot)
            self.sh_lot_no=lot.lot_name
            self.sh_expiration_date=lot.expiration_date
            # self.lot_id=lot.id




