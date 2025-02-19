from odoo import fields,models,api
from datetime import datetime

class Patient(models.Model):
    _name="sh.patient"
    _description="table for manage all patients"
    
    name=fields.Char()
    # dob=fields.Date()
    age=fields.Integer()
    # age=fields.Integer(compute="_age_calculate",store=True)
    doctor_id=fields.Many2one('sh.doctor',string="doctor data")
    
    diagnosis_ids=fields.Many2many('sh.diagnosis')
    
    cat_id=fields.Many2one('sh.age.category',string="patient category")
    
    
    # @api.depends('dob')
    # def _age_calculate(self):
    #     for record in self: 
    #         if record.dob:
                
    #             now=datetime.now()
    #             current=int(now.strftime("%Y")) 
    #             dob1=int(record.dob.strftime("%Y"))
    #             if dob1 < current:
                    
    #                 print("\n\n\n",dob1)
    #                 print("\n\n\n",current)
    #                 record.age=current-dob1 
    #             else: 
    #                 record.age=0     
    #         else:
    #             record.age=0 
    
    @api.model_create_multi
    def create(self,val_list):
        for record in val_list:
            print("\n\n\n\n<<<<<<<<<",val_list)
            # if record['age']:
                # if record['age']>0 and record['age']<=5:
                #     record['cat_id']=2
                    
                # if record['age']>5 and record['age']<=10:
                #     record['cat_id']=3
                    
                # if record['age']>10 and record['age']<=18:
                #     record['cat_id']=4
                    
                # if record['age']>18:
                #     record['cat_id']=5
            age=record['age']
            ans=self.env['sh.age.category'].search([('min_age','<=',age),('max_age','>=',age)])
            record['cat_id']=ans.id
                    
        
        res=super(Patient,self).create(val_list)
        return res



