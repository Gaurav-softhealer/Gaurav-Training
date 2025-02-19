from odoo import fields,models,api
from datetime import datetime

class Compute(models.Model):
    _name="sh.compute"
    _description="this computes table"
    
    amount=fields.Float()
    total_amount=fields.Float(compute="_calculate_price")
    
    dob=fields.Date()
    age=fields.Integer(compute="_age_calculate",store=True)
    
    meter=fields.Float()
    km=fields.Float(compute="_calculate_km") 
    
    @api.depends('amount')
    def _calculate_price(self):
        for record in self:
            record.total_amount=2.0*record.amount
    
    # def _inverse_total(self):
    #     for record in self:
    #         record.amount=record.total_amount/2.0
            
    @api.depends('dob')
    def _age_calculate(self):
        for record in self: 
            if record.dob:
                
                now=datetime.now()
                current=int(now.strftime("%Y")) 
                dob1=int(record.dob.strftime("%Y"))
                if dob1 < current:
                    
                    print("\n\n\n",dob1)
                    print("\n\n\n",current)
                    record.age=current-dob1 
                else: 
                    record.age=0     
            else:
                record.age=0 
                
          
    
    @api.depends('meter')
    def _calculate_km(self):
        for record in self:
            record.km=record.meter/1000   
            
            
            
    quantity=fields.Integer()
    price=fields.Integer()
    total=fields.Integer(compute="_price_item")
    
    @api.depends('quantity','price')
    def _price_item(self):
        for record in self:
            record.total=record.quantity*record.price
            
            
        
            