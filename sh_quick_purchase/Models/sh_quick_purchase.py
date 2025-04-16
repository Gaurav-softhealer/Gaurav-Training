from odoo import fields,models

class ShQuickPurchase(models.Model):
    _inherit="purchase.order"
    
    search_vendor=fields.Selection([
        ('all','All'),
        ('current_vendor','Current Vendor')
    ],default='all')
    
    search_data=fields.Char()
    
    filter=fields.Selection([
        ('all','All'),
        ('name','Name'),
        ('internal_ref','Internal Reference'),
        ('barcode','Barcode'),
        ('vendor_name','Vendor Name'),
        ('vendor_code','Vendor Code'),
        ('attribute','Attribute'),
        ('attribute_value','Attribute Value')   
    ],default='all')
    
    sh_purchase_line_ids=fields.One2many('sh.quick.purchase.line','sh_purchase_id')

    def Load_product(self):
        print(f"\n\n\n\t--------------> 27 ","Load product")
        
        if self.search_vendor=='all':
            if self.filter=='all':
                answer=self.env['product.product'].search([('name','ilike',self.search_data)])
                print(f"\n\n\n\t--------------> 31 ",answer)
                for rec in answer:
                    vals={
                        'product_id':rec.id
                    }
                    self.sh_purchase_line_ids=[(0,0,vals)]
            elif self.filter=='name':
                self.sh_purchase_line_ids=[(5,0,0)]
                answer=self.env['product.product'].search([('name','ilike',self.search_data)])
                print(f"\n\n\n\t--------------> 31 ",answer)
                for rec in answer:
                    vals={
                        'product_id':rec.id
                    }
                    self.sh_purchase_line_ids=[(0,0,vals)]
            elif self.filter=='internal_ref':
                self.sh_purchase_line_ids=[(5,0,0)]
                answer=self.env['product.product'].search([('default_code','ilike',self.search_data)])
                print(f"\n\n\n\t--------------> 31 ",answer)
                for rec in answer:
                    vals={
                        'product_id':rec.id
                    }
                    self.sh_purchase_line_ids=[(0,0,vals)]
            elif self.filter=='barcode':
                self.sh_purchase_line_ids=[(5,0,0)]
                answer=self.env['product.product'].search([('barcode','ilike',self.search_data)])
                print(f"\n\n\n\t--------------> 31 ",answer)
                for rec in answer:
                    vals={
                        'product_id':rec.id
                    }
                    self.sh_purchase_line_ids=[(0,0,vals)]
            elif self.filter=='attribute':
                self.sh_purchase_line_ids=[(5,0,0)]
                answer=self.env['product.product'].search([('attribute_line_ids.attribute_id','ilike',self.search_data)])
                print(f"\n\n\n\t--------------> 31 ",answer)
                for rec in answer:
                    vals={
                        'product_id':rec.id
                    }
                    self.sh_purchase_line_ids=[(0,0,vals)]
            elif self.filter=='attribute_value':
                self.sh_purchase_line_ids=[(5,0,0)]
                answer=self.env['product.product'].search([('attribute_line_ids.value_ids','ilike',self.search_data)])
                print(f"\n\n\n\t--------------> 31 ",answer)
                for rec in answer:
                    vals={
                        'product_id':rec.id
                    }
                    self.sh_purchase_line_ids=[(0,0,vals)]
                    
            elif self.filter=='vendor_name':
                self.sh_purchase_line_ids=[(5,0,0)]
                answer=self.env['product.product'].search([('seller_ids.partner_id.name','ilike',self.search_data)])
                print(f"\n\n\n\t--------------> 31 ",answer)
                for rec in answer:
                    vals={
                        'product_id':rec.id
                    }
                    self.sh_purchase_line_ids=[(0,0,vals)]
                    
            elif self.filter=='vendor_code':
                self.sh_purchase_line_ids=[(5,0,0)]
                answer=self.env['product.product'].search([('seller_ids.product_code','ilike',self.search_data)])
                print(f"\n\n\n\t--------------> 31 ",answer)
                for rec in answer:
                    vals={
                        'product_id':rec.id
                    }
                    self.sh_purchase_line_ids=[(0,0,vals)]
                    
        if self.search_vendor=='current_vendor':
            if self.filter=='name':
                self.sh_purchase_line_ids=[(5,0,0)]
                answer=self.env['product.product'].search([('name','ilike',self.search_data),('seller_ids.partner_id','=',self.partner_id.id)])
                print(f"\n\n\n\t--------------> 31 ",answer)
                for rec in answer:
                    vals={
                        'product_id':rec.id
                    }
                    self.sh_purchase_line_ids=[(0,0,vals)]
                    
            elif self.filter=='internal_ref':
                self.sh_purchase_line_ids=[(5,0,0)]
                answer=self.env['product.product'].search([('default_code','ilike',self.search_data),('seller_ids.partner_id','=',self.partner_id.id)])
                print(f"\n\n\n\t--------------> 31 ",answer)
                for rec in answer:
                    vals={
                        'product_id':rec.id
                    }
                    self.sh_purchase_line_ids=[(0,0,vals)]
            elif self.filter=='barcode':
                self.sh_purchase_line_ids=[(5,0,0)]
                answer=self.env['product.product'].search([('barcode','ilike',self.search_data),('seller_ids.partner_id','=',self.partner_id.id)])
                print(f"\n\n\n\t--------------> 31 ",answer)
                for rec in answer:
                    vals={
                        'product_id':rec.id
                    }
                    self.sh_purchase_line_ids=[(0,0,vals)]
            elif self.filter=='attribute':
                self.sh_purchase_line_ids=[(5,0,0)]
                answer=self.env['product.product'].search([('attribute_line_ids.attribute_id','ilike',self.search_data),('seller_ids.partner_id','=',self.partner_id.id)])
                print(f"\n\n\n\t--------------> 31 ",answer)
                for rec in answer:
                    vals={
                        'product_id':rec.id
                    }
                    self.sh_purchase_line_ids=[(0,0,vals)]
            elif self.filter=='attribute_value':
                self.sh_purchase_line_ids=[(5,0,0)]
                answer=self.env['product.product'].search([('attribute_line_ids.value_ids','ilike',self.search_data),('seller_ids.partner_id','=',self.partner_id.id)])
                print(f"\n\n\n\t--------------> 31 ",answer)
                for rec in answer:
                    vals={
                        'product_id':rec.id
                    }
                    self.sh_purchase_line_ids=[(0,0,vals)]
                    
            elif self.filter=='vendor_name':
                self.sh_purchase_line_ids=[(5,0,0)]
                answer=self.env['product.product'].search([('seller_ids.partner_id.name','ilike',self.search_data),('seller_ids.partner_id','=',self.partner_id.id)])
                print(f"\n\n\n\t--------------> 31 ",answer)
                for rec in answer:
                    vals={
                        'product_id':rec.id
                    }
                    self.sh_purchase_line_ids=[(0,0,vals)]
                    
            elif self.filter=='vendor_code':
                self.sh_purchase_line_ids=[(5,0,0)]
                answer=self.env['product.product'].search([('seller_ids.product_code','ilike',self.search_data),('seller_ids.partner_id','=',self.partner_id.id)])
                print(f"\n\n\n\t--------------> 31 ",answer)
                for rec in answer:
                    vals={
                        'product_id':rec.id
                    }
                    self.sh_purchase_line_ids=[(0,0,vals)]
            
                
        
    def add_product(self):
        print(f"\n\n\n\t--------------> 30 ","Add Product")
        if self.search_vendor=='all':
            if self.filter=='all':
                answer=self.env['product.product'].search([('name','ilike',self.search_data)])
                print(f"\n\n\n\t--------------> 31 ",answer)
                for rec in answer:
                    vals={
                        'product_id':rec.id
                    }
                    self.order_line=[(0,0,vals)]
            elif self.filter=='name':
                # self.sh_purchase_line_ids=[(5,0,0)]
                answer=self.env['product.product'].search([('name','ilike',self.search_data)])
                print(f"\n\n\n\t--------------> 31 ",answer)
                for rec in answer:
                    vals={
                        'product_id':rec.id
                    }
                    self.order_line=[(0,0,vals)]
            elif self.filter=='internal_ref':
                # self.sh_purchase_line_ids=[(5,0,0)]
                answer=self.env['product.product'].search([('default_code','ilike',self.search_data)])
                print(f"\n\n\n\t--------------> 31 ",answer)
                for rec in answer:
                    vals={
                        'product_id':rec.id
                    }
                    self.order_line=[(0,0,vals)]
            elif self.filter=='barcode':
                # self.sh_purchase_line_ids=[(5,0,0)]
                answer=self.env['product.product'].search([('barcode','ilike',self.search_data)])
                print(f"\n\n\n\t--------------> 31 ",answer)
                for rec in answer:
                    vals={
                        'product_id':rec.id
                    }
                    self.order_line=[(0,0,vals)]
            elif self.filter=='attribute':
                # self.sh_purchase_line_ids=[(5,0,0)]
                answer=self.env['product.product'].search([('attribute_line_ids.attribute_id','ilike',self.search_data)])
                print(f"\n\n\n\t--------------> 31 ",answer)
                for rec in answer:
                    vals={
                        'product_id':rec.id
                    }
                    self.order_line=[(0,0,vals)]
            elif self.filter=='attribute_value':
                # self.sh_purchase_line_ids=[(5,0,0)]
                answer=self.env['product.product'].search([('attribute_line_ids.value_ids','ilike',self.search_data)])
                print(f"\n\n\n\t--------------> 31 ",answer)
                for rec in answer:
                    vals={
                        'product_id':rec.id
                    }
                    self.order_line=[(0,0,vals)]
                    
            elif self.filter=='vendor_name':
                # self.sh_purchase_line_ids=[(5,0,0)]
                answer=self.env['product.product'].search([('seller_ids.partner_id.name','ilike',self.search_data)])
                print(f"\n\n\n\t--------------> 31 ",answer)
                for rec in answer:
                    vals={
                        'product_id':rec.id
                    }
                    self.order_line=[(0,0,vals)]
                    
            elif self.filter=='vendor_code':
                # self.sh_purchase_line_ids=[(5,0,0)]
                answer=self.env['product.product'].search([('seller_ids.product_code','ilike',self.search_data)])
                print(f"\n\n\n\t--------------> 31 ",answer)
                for rec in answer:
                    vals={
                        'product_id':rec.id
                    }
                    self.order_line=[(0,0,vals)]
                    
        if self.search_vendor=='current_vendor':
            if self.filter=='name':
                # self.sh_purchase_line_ids=[(5,0,0)]
                answer=self.env['product.product'].search([('name','ilike',self.search_data),('seller_ids.partner_id','=',self.partner_id.id)])
                print(f"\n\n\n\t--------------> 31 ",answer)
                for rec in answer:
                    vals={
                        'product_id':rec.id
                    }
                    self.order_line=[(0,0,vals)]
                    
            elif self.filter=='internal_ref':
                # self.sh_purchase_line_ids=[(5,0,0)]
                answer=self.env['product.product'].search([('default_code','ilike',self.search_data),('seller_ids.partner_id','=',self.partner_id.id)])
                print(f"\n\n\n\t--------------> 31 ",answer)
                for rec in answer:
                    vals={
                        'product_id':rec.id
                    }
                    self.order_line=[(0,0,vals)]
            elif self.filter=='barcode':
                # self.sh_purchase_line_ids=[(5,0,0)]
                answer=self.env['product.product'].search([('barcode','ilike',self.search_data),('seller_ids.partner_id','=',self.partner_id.id)])
                print(f"\n\n\n\t--------------> 31 ",answer)
                for rec in answer:
                    vals={
                        'product_id':rec.id
                    }
                    self.order_line=[(0,0,vals)]
            elif self.filter=='attribute':
                # self.sh_purchase_line_ids=[(5,0,0)]
                answer=self.env['product.product'].search([('attribute_line_ids.attribute_id','ilike',self.search_data),('seller_ids.partner_id','=',self.partner_id.id)])
                print(f"\n\n\n\t--------------> 31 ",answer)
                for rec in answer:
                    vals={
                        'product_id':rec.id
                    }
                    self.order_line=[(0,0,vals)]
            elif self.filter=='attribute_value':
                # self.sh_purchase_line_ids=[(5,0,0)]
                answer=self.env['product.product'].search([('attribute_line_ids.value_ids','ilike',self.search_data),('seller_ids.partner_id','=',self.partner_id.id)])
                print(f"\n\n\n\t--------------> 31 ",answer)
                for rec in answer:
                    vals={
                        'product_id':rec.id
                    }
                    self.order_line=[(0,0,vals)]
                    
            elif self.filter=='vendor_name':
                # self.sh_purchase_line_ids=[(5,0,0)]
                answer=self.env['product.product'].search([('seller_ids.partner_id.name','ilike',self.search_data),('seller_ids.partner_id','=',self.partner_id.id)])
                print(f"\n\n\n\t--------------> 31 ",answer)
                for rec in answer:
                    vals={
                        'product_id':rec.id
                    }
                    self.order_line=[(0,0,vals)]
                    
            elif self.filter=='vendor_code':
                # self.sh_purchase_line_ids=[(5,0,0)]
                answer=self.env['product.product'].search([('seller_ids.product_code','ilike',self.search_data),('seller_ids.partner_id','=',self.partner_id.id)])
                print(f"\n\n\n\t--------------> 31 ",answer)
                for rec in answer:
                    vals={
                        'product_id':rec.id
                    }
                    self.order_line=[(0,0,vals)]

        
    # def selected_line(self):
    #     print(f"\n\n\n\t--------------> 40 ","single product selected")
    #     for record in self.sh_purchase_line_ids:
    #         print(f"\n\n\n\t--------------> 42 ",record)
    #         if record.is_selected:
            
    #             vals={
    #                 'product_id':self.product_id.id
    #             }
                
    #             self.order_line=[(0,0,vals)] 
    
    def selected_line(self):
        print("\n\n\n\t--------------> 40 ", "single product selected")
        lines = []
        for record in self.sh_purchase_line_ids:
            print("\n\n\n\t--------------> 42 ", record)
            if record.is_selected:
                vals = {
                    'product_id': record.product_id.id,
                }
                lines.append((0, 0, vals))

        self.order_line = lines
