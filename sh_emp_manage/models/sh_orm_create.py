from odoo import fields,models,api
import random

class Create(models.Model):
    _name="sh.orm.create"
    _description="this table is used to store data of orm create"
    
    stu_name=fields.Char()
    stu_age=fields.Integer()
    stu_no=fields.Integer()
    price=fields.Integer()
    gender=fields.Selection([
        ('male','Male'),
        ('female','Female'),
        ('other','Other')
    ])
    
    dep_id=fields.Many2one('sh.department')
    # job_ids=fields.One2many('sh.job','dep_id')
    parent=fields.Char()
    
    cat_ids=fields.Many2many('sh.emp.cat')
    
    @api.model_create_multi
    def create(self,val_list):
        for record in val_list:

            
            # print("\n\n\n\n\n\n$$$$$$$$$$$$$$$",val_list)
            # record['stu_no']=13434654
            
            # res=super(Create,self).create(val_list)
            # print("\n\n\n\n\n\n$$$$$$$$$$$$$$$",val_list)
            # print(type(res))
            # print(res)
            
            # return res    
            
            # if record['price']<0:
            #     record['price']=0
            
            # record['stu_no']=random.randrange(1,1000)
            
            # print(val_list)
            # record['gender']='male'
            
            
            # print(f"\n\n\n\t--------------> 44 val_list",val_list)
            # print("\n\n\n\n@@@@@@@@@@@@@",record)
            
            
            # print("\n\n\n\n@@@@@@@@@@@@@",record.dep_id.name)
            
            
            # record['cat_ids']=[(4, 1)]   
            
            print("\n\n\n\n\n******************",record.get('stu_name').upper())
            record['stu_name']=record.get('stu_name').upper()
            
            res=super(Create,self).create(val_list)
            # res.parent = res.dep_id.parent_dep_id.name
            return res    