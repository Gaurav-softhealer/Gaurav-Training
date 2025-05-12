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
    
    is_splitted=fields.Boolean()
    
    sh_customer_allergy_ids=fields.Many2many('sh.allergy',string="Customer Allergies")

    def action_confirm(self):
        res= super().action_confirm()
        if self.sh_doctor_id:
            if self.sh_doctor_id.doctor_commission_type=='by_patient':
                vals={
                    'date':datetime.today(),
                    'sh_so_id':self.id,
                    'patient_id':self.partner_id.id,
                    'sh_doctor_id':self.sh_doctor_id.id,
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
                    'sh_doctor_id':self.sh_doctor_id.id,
                    'sh_so_amount':self.amount_untaxed,
                    'doctor_commission_type':self.sh_doctor_id.doctor_commission_type,
                    'commission_rate':self.sh_doctor_id.commission_percent,
                    'dr_commission':ans    
                }
            
            self.sh_doctor_id.dr_commission_ids=[(0,0,vals)]
        print(f"\n\n\n\t--------------> 75 self.picking_ids.move_ids.lot_ids",self.picking_ids.move_ids.lot_ids)
        self.order_line.lot_ids = self.picking_ids.move_ids.lot_ids.ids
        return res
    

    def action_cancel(self):
        answer=self.env['sh.doctor.commission'].search([('sh_so_id','=',self.id)])
        print(f"\n\n\n\t--------------> 59 answer",answer)
        
        for record in answer:
            self.sh_doctor_id.dr_commission_ids=[(2,record.id)]
        return super().action_cancel()


    
    def split_sale_order(self):
        self.is_splitted=True
        return {
                'type': 'ir.actions.act_window',
                'name': 'Split Sale Order',
                'view_mode': 'form',
                'res_model': 'sale.order',
                'target': 'new',
                'context': {
                 
                }
            }
    

    @api.onchange('order_line')
    def check_narco(self):
        for record in self.order_line:
            print(f"\n\n\n\t--------------> 97 record.product_id.categ_id",record.product_id.categ_id.name)
            if record.product_id.categ_id.is_narcotics:
                self.is_narcotics=True
            else:
                self.is_narcotics=False
          
    @api.onchange('partner_id')
    def customer_allergies(self):
        if self.partner_id:
            self.sh_aadhar_card=self.partner_id.sh_aadhar_no
            self.sh_mobile_no=self.partner_id.phone
            self.sh_customer_allergy_ids=[(6,0,self.partner_id.sh_allergies_ids.ids)]


    @api.onchange("order_line")
    def find_lot_sn(self):
        for rec in self:
            for i in rec.order_line:
                rec_lot = self.env['stock.quant'].search([('product_id.id','=',i.product_id.id)])
                print(f"\n\n\n\t--------------> 29 rec_lot",rec_lot)
                lots_list =[]
                current_product_qty = i.product_uom_qty
                for j in rec_lot:
                    if j.available_quantity > 0 :
                        lots_list.append(j.lot_id.id)
                        current_product_qty = j.available_quantity - abs(current_product_qty)
                        if current_product_qty >= 0:
                            print(f"\n\n\n\t--------------> 41 lots_list",lots_list)
                            i.lot_ids = lots_list
                            break 
        
        
class ShPharmacyOrderLine(models.Model):
    _inherit="sale.order.line"
    
    is_selected=fields.Boolean()
    sh_lot_no=fields.Char(string="Lot No")
    sh_expiration_date=fields.Datetime()
    split_id=fields.Many2one('sh.split.sale.order')
    lot_ids=fields.Many2many('stock.lot')


class ShStockLot(models.Model):
    _inherit = 'stock.lot'

    @api.depends('name')
    def _compute_display_name(self):
        for template in self:
            template.display_name = False if not template.name else (
                '{}{}'.format(
                     template.name ,'[%s] ' % template.expiration_date if template.expiration_date else ''
                ))
    





