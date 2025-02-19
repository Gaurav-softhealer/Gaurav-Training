from odoo import fields,models,api

class Order(models.Model):
    _name="sh.sale.order.line"
    _description="this table is store data about order"
    
    name=fields.Char()
    
    order_id=fields.Many2one('sh.sale.order',string="order data")
    
    product_id=fields.Many2one('sh.product.product')
    quantity=fields.Integer()
    price=fields.Integer()
    
    tax_ids=fields.Many2many('sh.account.tax')
    
    total=fields.Integer(compute="_calculate_total")
    exclude_tax=fields.Integer(compute="_calculate_total")
    
    @api.depends('quantity','price','tax_ids')
    def _calculate_total(self):
        for record in self:
            # print("\n\n\n\n\n============>",record.tax_ids.tax)
            # tax=self.env['sh.account.tax'].browse(record.tax_ids)
            # print("\n\n\n\n\n============>",tax)
            # print("||||||||||||||||||||",tax.tax)
            print("\n\n\n\n\n&&&&&&&&&&&&&&&&&&&&>>>>>>>",record.tax_ids)
            for i in record.tax_ids:
                tax=i.tax
                print("....................>",tax)
                record.total=(tax/100)*(record.quantity*record.price)+(record.quantity*record.price)    
                record.exclude_tax=(record.quantity*record.price) 
            
            # for i in tax:
            #     print("++++++++++++++++++>",i.tax)
            # record.total=(record.quantity*record.price)*tax.tax / (100+tax.tax) 
            # record.total=(record.quantity*record.price)
    # total_amount=fields.Integer()        