from odoo import fields, models, api
from datetime import datetime,timedelta

class SaleOrderHistory(models.Model):
    _name="sh.sale.order.history"
    _description="This model is used to manage sale order history"
    
    sh_sale_order_id=fields.Many2one('sale.order',string="sale order")
    sh_sale_order_name=fields.Char()
    order_date=fields.Date()
    product_id=fields.Many2one('product.product')
    product=fields.Many2one('product.template')
    price=fields.Float()
    new_price=fields.Float()
    quantity=fields.Float()
    discount=fields.Float()
    subtotal=fields.Float()
    all_selected=fields.Boolean()
    state=fields.Char()
    
    def reorder_button(self):

        result=self.env['sale.order'].browse(self.sh_sale_order_id.id)
        print(f"\n\n\n\t--------------> 23 result",result)

        vals={
            'name':self.product_id.name,
            'product_id':self.product_id.id,
            # 'order_id':result.id,
            'product_template_id':self.product_id.id
        }
        result.order_line=[(0,0,vals)]


    def View_button(self):

        answer=self.env['sale.order'].search([('name','=',self.sh_sale_order_name)])
        print(f"\n\n\n\t--------------> 60 answer",answer)
        return{
            'type': 'ir.actions.act_window',
            'name': 'Reorder form',
            'view_mode': 'form',
            'res_model': 'sale.order',
            'domain': [('name', '=', self.sh_sale_order_name)],  
            'res_id':answer.id,
        }

    

class SaleOrderHistoryInherit(models.Model):
    _inherit="sale.order"

    
    sale_order_history_ids=fields.One2many('sh.sale.order.history','sh_sale_order_id')
    
    @api.onchange('partner_id')
    def find_sale_history(self):

        lst=[]
        for i in self.company_id.sh_sale_stage:
            lst.append(i.key)
        
        today=datetime.today()    
        no_of_day=today-timedelta(days=self.company_id.sh_no_of_day)
        print(f"\n\n\n\t--------------> 118 days",no_of_day)
        print(f"\n\n\n\t--------------> 113 lst",lst)
        if self.partner_id:
            self.sale_order_history_ids=[(5,0,0)]

            
            result=self.env['sale.order.line'].search([('order_partner_id','=',self.partner_id.id),('state','=',lst),('order_id.date_order','>',no_of_day)],limit=self.company_id.sh_no_of_order)
            print(f"\n\n\n\t--------------> 46 result",result)
            for record in result:

                    vals={
                        'sh_sale_order_name':record.order_id.name,
                        'product_id':record.product_id.id,
                        'order_date':record.order_id.date_order,
                        'price':record.price_unit,
                        'quantity':record.product_uom_qty,
                        'state':record.state
                        
                    }

                    self.sale_order_history_ids=[(0, 0, vals)] 
            
    
    def all_sale_order(self):

        selected=self.env['sh.sale.order.history'].search([('sh_sale_order_id.id','=',self.id),('all_selected','=',True)])
        for i in selected:
            if i.all_selected:
                print(f"\n\n\n\t--------------> 144 i",i)
                
                vals={
                    'name':i.product_id.name,
                    'product_id':i.product_id.id,
                    'product_template_id':i.product_id.id
                }
                self.order_line=[(0,0,vals)]
        print(f"\n\n\n\t--------------> 131 called function","called function")        

class SaleOrderStage(models.Model):
    _name="sale.order.stage"
    _description="this model is used to manage the stages"
    
    name=fields.Char()
    key=fields.Char()
 
 
