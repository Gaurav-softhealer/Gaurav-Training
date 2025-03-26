from odoo import fields,models,api,Command

class AlternateWizard(models.TransientModel):
    _name="alternate.wizard"
    _description="this model is used to open the wizard"
  
    def default_get_data(self):
        
        active_id=self.env.context.get('active_ids')
        active_model=self.env.context.get('active_model')
        
        # res=super(AlternateWizard,self).default_get(fields)
        
        print(f"\n\n\n\t--------------> 16 ",active_id)
        print(f"\n\n\n\t--------------> 17 ",active_model)
        
        result=self.env[active_model].browse(active_id)
        
        print(f"\n\n\n\t--------------> 21 ",result)
        print(f"\n\n\n\t--------------> 22 ",result.id)
        print(f"\n\n\n\t--------------> 24 ",result.name)
        print(f"\n\n\n\t--------------> 28 ",result.product_id)
        # res['internal_ref']=result.name
        # return res
        return result.product_id.id
    
    
    # internal=fields.Char(default=default_get_data)
    internal_ref=fields.Many2one('product.product',default=default_get_data,readonly=True)
    replacing_product_id=fields.Many2one('product.product',string="Replacing Product")
    temp=fields.Char(compute="related_alternate")
    
    # @api.depends('internal_ref')
    # def related_alternate(self):
    #     print(f"\n\n\n\t--------------> 40 ","compute called")
    #     for record in self:
    #         if record.internal_ref:
    #             result=self.env['product.product'].search([('id','=',record.internal_ref.id)])
    #             print(f"\n\n\n\t--------------> 43 ",result)
    
    
    @api.depends('internal_ref')
    def related_alternate(self):
        print("\n\n\n\t--------------> Compute method called")
        for record in self:
            if record.internal_ref:
                result = self.env['product.product'].search([('id', '=', record.internal_ref.id)])
                print(f"\n\n\n\t--------------> 48 ",result)
                self.temp="hii"
                domain = [('id', 'in', result.alternative_ids.ids)]
                
            else:
                domain=[]
            record.temp=str(domain)

    
    def alternate_product(self):
        active_id=self.env.context.get('active_ids')
        active_model=self.env.context.get('active_model')
        
        print(f"\n\n\n\t--------------> 16 ",active_id)
        print(f"\n\n\n\t--------------> 17 ",active_model)
        
        result=self.env[active_model].browse(active_id)
        print(f"\n\n\n\t--------------> 67 ",result.product_id.alternative_ids.ids)
        
        return result.product_id.alternative_ids
    
    alternate_products=fields.Many2many('product.product', default=alternate_product)
        
        
    def replace_product(self):
        print(f"\n\n\n\t--------------> 73 ","Replace called")   
          
        active_id=self.env.context.get('active_ids')
        active_model=self.env.context.get('active_model')
        
        print(f"\n\n\n\t--------------> 16 ",active_id)
        print(f"\n\n\n\t--------------> 17 ",active_model)  
 
        result=self.env[active_model].browse(active_id)
        
        print(f"\n\n\n\t--------------> 83 ",result.product_id)
        print(f"\n\n\n\t--------------> 84 ",self.replacing_product_id)
        result.product_id=self.replacing_product_id
        