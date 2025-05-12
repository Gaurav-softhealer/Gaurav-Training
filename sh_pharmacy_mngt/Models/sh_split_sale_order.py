from odoo import fields,models,api
from odoo.exceptions import UserError, ValidationError

class ShSplitSaleOrder(models.Model):
    _name="sh.split.sale.order"
    _description="this model is used to store data about split sale order"
    
    sh_partner_id=fields.Many2one('res.partner')
    sh_doctor_id=fields.Many2one('res.partner',domain=[('is_doctor','=',True)])
    sh_prescription=fields.Binary(string="Upload Prescription")
    
    sh_mobile_no=fields.Char(string="Mobile Number")
    sh_aadhar_card=fields.Char(string="Aadhar Card Number")
    is_narcotics=fields.Boolean()
    
    sh_split_order_ids=fields.One2many('sh.split.sale.order.data','sh_split_id')
    
    def default_get(self, fields_list):
        res=super().default_get(fields_list)
        
        active_id=self.env.context.get('active_ids')
        active_model=self.env.context.get('active_model')
        
        answer=self.env[active_model].browse(active_id)
        print(f"\n\n\n\t--------------> 20 answer",answer)
        
        res['sh_partner_id']=answer.partner_id.id
        res['sh_prescription']=answer.sh_prescription
        
        lst=[]
        for record in answer.order_line:
            if record.is_selected:
                    if record.product_id.categ_id.is_narcotics:
                        res['is_narcotics']=True
                    lst.append((0,0,{'product_id':record.product_id.id,
                        'product_qty':1.0,
                        'product_uom':record.product_uom.id,
                        'price_unit':record.price_unit}))
            
        res['sh_split_order_ids']=lst   
        return res     
        
    def split_sale_quantity(self):
        print(f"\n\n\n\t--------------> 20 ","Wizard save button created")

        active_id=self.env.context.get('active_ids')
        active_model=self.env.context.get('active_model')
        
        answer=self.env[active_model].browse(active_id)
        print(f"\n\n\n\t--------------> 15 answer",answer)
        
        # for i in answer.order_line:
        for j in self.sh_split_order_ids:
                
                print(f"\n\n\n\t--------------> 64 self.is_narcotics",self.is_narcotics)
                
                ans=self.env['sale.order.line'].search([('order_id','=',answer.id),('product_id','=',j.product_id.id)])
                print(f"\n\n\n\t--------------> 52 answer",answer)

                if ans.product_uom_qty<j.product_qty:
                    raise ValidationError('You enter More Quanity then exist in original sale order')

                if ans.product_uom_qty==j.product_qty:
                    ans.unlink()
                    
                else:
                    print(f"\n\n\n\t--------------> 60 j",j)
                    result=ans.product_uom_qty-j.product_qty
                    ans.write({
                        'product_uom_qty':result
                    })

    @api.model_create_multi
    def create(self, vals_list):
        res= super().create(vals_list) 
        
        active_id=self.env.context.get('active_ids')
        active_model=self.env.context.get('active_model')
        
        answer=self.env[active_model].browse(active_id)
        
        vals={
                'partner_id':res.sh_partner_id.id,
                'sh_doctor_id':res.sh_doctor_id.id,
                'sh_prescription':res.sh_prescription,
                'sh_mobile_no':res.sh_mobile_no,
                'sh_aadhar_card':res.sh_aadhar_card,
                
            }
        ans=self.env['sale.order'].create(vals)
        lst=[]
        
        for record in res.sh_split_order_ids:
            lst.append((0,0,{'product_id':record.product_id.id,'product_uom_qty':record.product_qty,'price_unit':record.price_unit,}))
        ans.order_line=lst  
        answer.find_lot_sn()
        ans.find_lot_sn()
        return res
    