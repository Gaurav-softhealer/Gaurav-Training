from odoo import fields,models,api

class ShQuickPurchaseLine(models.Model):
    _name="sh.quick.purchase.line"
    _description="This model is used to store data about quick purchase line"
    
    product_id=fields.Many2one('product.product')
    description=fields.Char(related='product_id.name',string="description")
    cost=fields.Float(related='product_id.standard_price')
    unit_price=fields.Float(related='product_id.lst_price')
    quantity=fields.Float(default=1.0)
    on_hand=fields.Float(related='product_id.qty_available')
    forcast_qty=fields.Float(related='product_id.virtual_available')
    sh_purchase_id=fields.Many2one('purchase.order')
    is_selected=fields.Boolean(string="Select")
    
    
    def sh_quick_buy(self):
        print(f"\n\n\n\t--------------> 18 ","add the product")
        print(f"\n\n\n\t--------------> 19 self.product_id",self.product_id)
        vals={
            'product_id':self.product_id.id
        }
        
        self.sh_purchase_id.order_line=[(0,0,vals)] 