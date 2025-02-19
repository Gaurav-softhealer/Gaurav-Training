from odoo import fields,models,api
import random

class Employee(models.Model):
    _name="sh.orm.employee"
    _description="this table is used to store data of orm employee"
    
    name=fields.Char()
    cat_ids=fields.Many2many('sh.orm.category',string="category name")
    ref=fields.Char()
    mobile=fields.Char()
    salary=fields.Integer()
    statusbar=fields.Selection([
        ('confirm','Confirm'),
        ('done','Done')
    ])
    
    
    @api.model_create_multi
    def create(self,val_list):
        # print("\n\n\n\n!!!!!!!!!!!!!!!!",self,val_list)
        for record in val_list:
            # print("\n\n\n\n***************",record['cat_ids'])
            print("\n\n\n&&&&&&&&&&&",val_list)
            print("\n\n\n&&&&&&&&&&&",record)
            # for i in record:
            #     print("\n\n\n&&&&&&&&&&&",i)
            # print("\n\n\n\n!!!!!!!!!!!!!!!!",record['cat_id'])
            # record['ref']=record['cat_id']
            # ref=self.env['sh.orm.category'].browse(record['cat_ids'])
            
            # print("\n\n\n\n#############",ref)
            # record['ref']=ref.ref
            
            
            if record['mobile']:
                if '+91' not in record['mobile']:
                    record['mobile']=f"+91 {record['mobile']}"
            
            
            
            
            
            res=super(Employee,self).create(val_list)
              
            # for rec in res.cat_ids:
                # print("\n\n\n\n\n\n\n\n\n\n\n",type(rec)) 
                # print("\n\n\n\nthis is rec record:",rec)  
                # print(type(rec.ref))
                # print((rec.ref))
            return res
    
    
        
    
    def write(self,vals):
        print("\n\n\n\n$$$$$$$$$$$",self,vals)
        # ref=self.env['sh.orm.category'].browse(vals['cat_ids'])
        # print("\n\n\n\n#############",ref)
        # vals['ref']=ref.ref
        
        if vals['mobile':]:
            if '+91' not in vals['mobile']:
                vals['mobile']=f"+91 {vals['mobile']}"
            if len(vals['mobile'])<14:
                # raise ValueError("enter bigger number")
                print("\n\n\n\n\nenter bigger number")
                
        res=super(Employee,self).write(vals)
        print("\n\n\n\n\n+++++++++++",res)
        return res    
    
    
