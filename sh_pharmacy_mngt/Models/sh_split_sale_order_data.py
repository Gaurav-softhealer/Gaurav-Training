from odoo import fields,models,api

class SplitOrderData(models.Model):
    _name="sh.split.sale.order.data"
    _description="this table used for split order data"
    
    sh_split_id=fields.Many2one('sh.split.sale.order')
    product_id=fields.Many2one('product.product')
    product_qty=fields.Float()
    product_uom=fields.Many2one('uom.uom')
    price_unit=fields.Float()
    # tax_id=fields.
    # 'product_uom_qty': record.product_uom_qty,
    #                 'product_uom': record.product_uom.id, 
    #                 'price_unit': record.price_unit,
    #                 'name': record.name,
                    # 'tax_id': [(6, 0, record.tax_id.ids)]
   
   
   
   
   
    # @api.model_create_multi
    # def create(self, vals_list):
    #         for record in vals_list:
    #             split_id = record.get('sh_split_id')
                
    #             if split_id:
    #                 split_rec = self.env['sh.split.sale.order'].browse(split_id)
                    
    #                 vals = {
    #                     'partner_id': split_rec.sh_partner_id.id
    #                 }
    #                 ans=self.env['sale.order'].create(vals)
                    
    #                 for i in split_rec.sh_split_order_ids:
    #                     vals2={
    #                         'order_id':ans.id,
    #                         'product_id':i.product_id.id,
    #                         'product_uom_qty':i.product_qty,
    #                         'price_unit':i.price_unit
    #                     }
    #                     self.env['sale.order.line'].create(vals2)
            
    #         return super().create(vals_list)
    
    
    


                 
                    
    # @api.model_create_multi
    # def create(self, vals_list):
    #     for record in vals_list:
    #         print(f"\n\n\n\t--------------> 23 self.",record['sh_split_id'].sh_partner_id.id)
            
    #         vals={
    #             'partner_id':self.sh_split_id.sh_partner_id.id
    #         }
            
    #         self.env['sale.order'].create(vals)
            
    #         return super().create(vals_list)