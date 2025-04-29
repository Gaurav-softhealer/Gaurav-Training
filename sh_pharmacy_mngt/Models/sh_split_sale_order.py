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
    # sh_split_ids=fields.One2many('sale.order.line','split_id')
    # sh_split_sale_ids=fields.Many2many('sale.order.line')
    
    sh_split_order_ids=fields.One2many('sh.split.sale.order.data','sh_split_id')
    
    def default_get(self, fields_list):
        res=super().default_get(fields_list)
        
        active_id=self.env.context.get('active_ids')
        active_model=self.env.context.get('active_model')
        
        answer=self.env[active_model].browse(active_id)
        print(f"\n\n\n\t--------------> 20 answer",answer)
        
        # for record in answer.order_line:
        #     ...
        
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
                    # ans.order_id.order_line=[(4,0)]
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
        return res
    
    
          
        # print(f"\n\n\n\t--------------> 73 self",self)
        # for record in vals_list:
        #     partner_id = record.get('sh_partner_id')
        #     sh_split_order_ids=record.get('sh_split_order_ids')
        #     vals={
        #         'partner_id':partner_id
        #     }
        #     ans=self.env['sale.order'].create(vals)
        #     lst=[]
            
        #     print(f"\n\n\n\t--------------> 82 sh_split_order_ids",sh_split_order_ids)
            
        #     for rec in self.sh_split_order_ids:
        #         print(f"\n\n\n\t--------------> 86 rec",rec)
        #         order_list=(0,0,{
        #             'order_id':ans.id,
        #             'product_id':rec.product_id.id,
        #             'product_uom_qty':rec.product_uom,
        #             # 'product_uom':record.product_uom.id,
        #             'price_unit':rec.price_unit})
                
        #         lst.append(order_list)
        #     ans.order_line=lst
       
        
        
    #         @api.model_create_multi
    # def create(self, vals_list):

    #     res = super().create(vals_list)
    #     rec_so = self.env[self.env.context.get('active_model')].browse(self.env.context.get("active_ids"))
    #     print(f"\n\n\n\t--------------> 36 rec_so",rec_so)
    #     print(f"\n\n\n\t--------------> 47 res",res)
    #     for rec in res.sh_order_line_ids:
    #         for i in rec_so.order_line:
    #             if i.product_id.id == rec.product_id.id:
    #                 if i.product_uom_qty - rec.quantity < 0:
    #                     raise ValidationError("The quantity of "+i.product_id.name+" is invalid")
    #                 elif i.product_uom_qty - rec.quantity == 0:
    #                     rec_so.order_line = [Command.unlink(i.id)]
    #                 else:
    #                     i.product_uom_qty = i.product_uom_qty - rec.quantity

    #     rec_new_so = self.env['sale.order'].create({'partner_id':res.name.id,'doctor_id':res.doctor_id})
    #     sol_lines = []
    #     for rec in res.sh_order_line_ids:
    #         sol_lines.append((0,0,{'product_id':rec.product_id.id,'product_uom_qty':rec.quantity,'price_unit':rec.unit_price,'tax_id':rec.tax_ids.ids}))

    #     rec_new_so.order_line = sol_lines


    #     return res
        
        
    #     # for record in answer.order_line:
    #     #     for i in res['sh_split_order_ids']:
    #     # print(f"\n\n\n\t--------------> 18 record",record)
    #     # print(f"\n\n\n\t--------------> 19 record.product_id.name",record.product_id.name)
    #     # print(f"\n\n\n\t--------------> 19 record.product_id.id",record.product_id.id)
    #             # i.product_id=record.product_id.id
                
    #     active_id=self.env.context.get('active_ids')
    #     active_model=self.env.context.get('active_model')
            
    #     print(f"\n\n\n\t--------------> 78 active_id",active_id)
    #     print(f"\n\n\n\t--------------> 79 active_model",active_model)
        
    #     answer=self.env[active_model].browse(active_id)

        
                
    #     ans=self.env['sale.order'].create({
    #         'partner_id':answer.partner_id.id
    #     })  
        
    #     sol_lines = []
        

    #     for rec in answer.order_line:
    #         line_vals = (0, 0, {
    #             'order_id':ans.id,
    #             'product_id': rec.product_id.id,
    #             # 'product_uom_qty': 1,
    #             # 'product_uom': rec.product_uom.id,  
    #             # 'price_unit': rec.price_unit,   
    #         })
    #         sol_lines.append(line_vals)

    #     # ans.order_line = sol_lines      
                
    #     res.update({'sh_split_ids':sol_lines})
    #     return res
    
    

    
    # # def split_sale_quantity(self):
    # #     print(f"\n\n\n\t--------------> 166 ","Quantity Split")
        
    # #     for i in self.sh_split_sale_ids:
    # #         # print(f"\n\n\n\t--------------> 40 ",self.sh_split_sale_ids)
    # #         for j in i.product_id:
    # #             # print(f"\n\n\n\t--------------> 42 ",i.product_id)
    # #             self.env['sale.order.line'].create({
    # #                 'product_id':j.id
    # #             })
    
    
    # def split_sale_quantity(self):
    #     print(f"\n\n\n\t--------------> 46 self",self)
    #     print(f"\n\n\n\t--------------> 50 ",self.sh_partner_id.name)

        
            
            
    #     # sol_lines = []
        

    #     # for rec in self.sh_split_ids:
    #     #     line_vals = (0, 0, {
    #     #         'product_id': rec.product_id.id,
    #     #         'product_uom_qty': 1,
    #     #         'product_uom': rec.product_uom.id,  
    #     #         'price_unit': rec.price_unit,   
    #     #     })
    #     #     sol_lines.append(line_vals)

    #     # ans.order_line = sol_lines


    #     # active_id=self.env.context.get('active_ids')
    #     # active_model=self.env.context.get('active_model')
            
    #     # print(f"\n\n\n\t--------------> 78 active_id",active_id)
    #     # print(f"\n\n\n\t--------------> 79 active_model",active_model)
        
    #     # answer=self.env[active_model].browse(active_id)

        
    #     for record in answer.order_line:
    #         print(f"\n\n\n\t--------------> 79 record",record)
    #         # for i in record.product_
    #         # print(f"\n\n\n\t--------------> 35 record.product_uom_qty",record.product_uom_qty)
    #         # print(f"\n\n\n\t--------------> 33 record.product_uom_qty",record.product_uom_qty)
            
            
    #         ans=self.env['sale.order.line'].search([('order_id','=',answer.id),('product_id','=',record.product_id.id)])
    #         print(f"\n\n\n\t--------------> 36 ans",ans)
            
            
    #         for j in self.sh_split_ids:
                
    #             result=ans.product_uom_qty-j.product_uom_qty
                
            
            
    #         ans.write({
    #             'product_uom_qty':result
    #         })
    #     return ans
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        # sol_lines = []
 
        # rec_split_so = self.env['sale.order'].create({'partner_id':rec_so.partner_id.id})
 
        # for rec in rec_so.order_line:
        #             # split_sol_rec = self.env['sale.order.line'].create({'order_id':rec_split_so.id,'product_id':rec.product_id.id,'product_template_id':rec.product_id.id,'product_uom_qty':1,})
        #     lines = (0,0,{'order_id':rec_split_so.id,'product_id':rec.product_id.id,'product_uom_qty':1})
        #     sol_lines.append(lines)
        #     print(f"\n\n\n\t--------------> 20 split_sol_rec",sol_lines)
        # res.update({'sh_order_line_ids':sol_lines})
        # return res