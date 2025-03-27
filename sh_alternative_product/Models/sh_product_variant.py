from odoo import fields,models,api

class ProductVariant(models.Model):
    _inherit="product.product"
    
    data=fields.Char(string="data")
    alternative_ids=fields.Many2many(comodel_name='product.product',relation='my_model_partner_rel',column1='first',column2='second',)


    def write(self,vals):
        
        print(f"\n\n\n\t--------------> 12 ",vals)
        res= super(ProductVariant,self).write(vals)
        
        list=[]
        if 'alternative_ids' in vals:
            print(f"\n\n\n\t--------------> 17 ",vals['alternative_ids'])
            for i in vals['alternative_ids']:
                print(f"\n\n\n\t--------------> 19 ",i[0])
                if i[0]==4:
                    # list.append(i[1])
                    # print(f"\n\n\n\t--------------> 23 ",list)
                    
                    print("\n\n\n\n",i)
                    result=self.env['product.product'].browse(i[1])
                    print(f"\n\n\n\t--------------> 27 ",result)
        
                    for j in result.alternative_ids:
                        list.append(j.id)
                    print(f"\n\n\n\t--------------> 31 ",list)
                    
                    if self.id not in result.alternative_ids.ids:
                        result.write({'alternative_ids':[(4,self.id)]})
                    
                    print(f"\n\n\n\t--------------> 36 ",result.ids) 
                    for record in self.alternative_ids: 
                        print(f"\t--------------> 38 ",record.id)
                        print(f"\n\n\n\t--------------> 39 ",result.id)
                        if record.id not in list and record.id != result.id:
                            result.write({'alternative_ids':[(4,record.id)]})
                       
                elif i[0]==3:

                    print(f"\n\n\n\t--------------> 84 ","unlink callled")
                    print(f"\n\n\n\t--------------> 85 ",i)
                    
                    list.append(i[1])
                    print(f"\n\n\n\t--------------> 88 ",list)
                    
                    for record in list:
                        result=self.env['product.product'].browse(record)
                        
                        print(f"\n\n\n\t--------------> 93 ",result)
                        print(f"\n\n\n\t--------------> 94 ",self.id)
                        if self.id in result.alternative_ids.ids:
                            result.write({'alternative_ids':[(3,self.id)]})
                        print(f"\n\n\n\t--------------> 96 ",self.alternative_ids)
                        for j in self.alternative_ids:
                            if result.id in j.alternative_ids.ids and j.id == result.id:
                                result.write({'alternative_ids':[(3,result.id)]})
                        
                    
        return res

    
class SaleOrderline(models.Model):
    _inherit='sale.order.line'
    
    data=fields.Char()
    
    def open_wizard_alternate(self):
        
        print(f"\n\n\n\t--------------> 59 ","Alternative product wizard open")
        return {
            'type': 'ir.actions.act_window',
            'name': 'Alternative Product Wizard',
            'view_mode': 'form',
            'res_model': 'alternate.wizard',
            'target': 'new',
        }
       