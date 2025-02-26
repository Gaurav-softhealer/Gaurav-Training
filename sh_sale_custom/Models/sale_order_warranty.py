from odoo import fields,models,api
from datetime import datetime


class OrderWarranty(models.Model):
    _inherit = "sale.order"

    warranty = fields.Boolean()
    warranty_ids=fields.One2many('sh.sale.warranty','sale_order_id')
    warranty_period=fields.Integer(default=365)

    # @api.onchange('warranty')
    # def _find_date(self):
    #     if self.warranty:
    #         self.warranty_period=365

        
    warranty_expiry=fields.Date()   
    @api.model_create_multi
    def create(self,vals):
        for record in vals:
            res=super(OrderWarranty,self).create(vals)
            if res.warranty:
                vals_list = {
                    'sale_order_id':res.id,
                    'name': res.partner_id.name,
                    'order_date': res.date_order,
                    'warranty_period':res.warranty_period    
                }
                self.env['sh.sale.warranty'].create(vals_list)
            # res.warranty_expiry=res.warranty_ids.warranty_expiry_date
            return res 

    def write(self,vals):
        # print("??????????????????",vals) 
        # print("***********************",vals['date_order'])
        # print(f"\n\n\n\t--------------> 37 ",self)  
            res=super(OrderWarranty,self).write(vals)   
            ans=self.env['sh.sale.warranty'].search([('sale_order_id','=',self.id)])
            print("##########################",ans.read())
            print("***********************",vals['date_order'])
            if ans.order_date!=vals['date_order']:
            # if vals['date_order']!=self.date_order:
                vals_list = {
                    'order_date': vals['date_order'],    
                }
                print(f"\n\n\n\t--------------> 47 ",vals_list)
                ans.order_date=vals['date_order']
                # ans.write({'order_date': vals['date_order']})
        # self.warranty_expiry=self.warranty_ids.warranty_expiry_date
            return res
   
    
    
    
    
    
    
    
    
    
  