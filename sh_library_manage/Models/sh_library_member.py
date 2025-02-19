from odoo import models,fields,api
from datetime import datetime

class Member(models.Model):
    _name="sh.library.member"
    _description="this model is used to manage data about member in library"
    
    name=fields.Char()
    email=fields.Char()
    status=fields.Boolean()
    phone=fields.Char()
    dob=fields.Date(string="Birth Date")
    age=fields.Integer(compute="_calculate_age")
    
    
    @api.depends('dob')
    def _calculate_age(self):
        for record in self:
            if record.dob:
                now=datetime.now()
                current=int(now.strftime("%Y")) 
                dob1=int(record.dob.strftime("%Y"))
                if dob1 < current:
                    record.age=current-dob1 
                else: 
                    record.age=0     
            else:
                record.age=0 
                
    # book_ids=fields.Many2many('sh.library.book',string="borrow books")  
    borrowed_books=fields.One2many("sh.library.borrow",'name',string="borrowed book")
    
    # membership_type=fields.Selection([
    #     ('regular','Regular'),
    #     ('premium','premium')
    # ],compute="_check_membership")  
    
    # @api.depends('book_ids')
    # def _check_membership(self):
    #     for record in self:
    #         if len(record.book_ids)<3:
    #             record.membership_type='regular'
    #         else:
    #             record.membership_type='premium'
                

    @api.model_create_multi
    def create(self,val_list):
        for record in val_list:
            email=record['email']
            check=self.env['sh.library.member'].search([('email','=',email)])
            print("##############",check)
            if check:
                record['status']=True
                
            if record['phone']:
                if '+91' not in record['phone']:
                    record['phone']=f"+91 {record['phone']}"
                
            res=super(Member,self).create(val_list)
            return res

            
            
    def write(self,vals):
        email=vals['email']
        check=self.env['sh.library.member'].search([('email','=',email)])
        if check:
            vals['status']=True
        else:
            vals['status']=False
        if self.phone:
            if '+91' not in self.phone:
                vals['phone']=f"+91 {vals['phone']}"

        res= super(Member,self).write(vals)
        return res
    