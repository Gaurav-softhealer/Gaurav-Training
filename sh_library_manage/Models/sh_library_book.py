from odoo import fields,models,api
from odoo.exceptions import UserError, ValidationError
import random

class Book(models.Model):
    _name="sh.library.book"
    _description="this model is used to store data about book in library"
    
    book_ref=fields.Integer()
    name=fields.Char()
    book_image=fields.Binary()
    book_subject=fields.Text()
    book_publisher=fields.Char()
    book_auther=fields.Char()
    book_pages=fields.Integer()
    book_quantity=fields.Integer()

        
    cat_id=fields.Many2one('sh.library.category',string="Category Name")
    
    borrow_ids=fields.Many2many('sh.library.borrow',string="who borrows books")
    
    status=fields.Selection([
        ('Cart','cart'),
        ('Borrowed','borrowed')
    ])
    
       
    @api.model_create_multi
    def create(self,val_list):
        for record in val_list:
            record['book_ref']=random.randrange(1000,9999)
            if not record['cat_id']:
                record['cat_id']=15
            else:
                record['cat_id']=record['cat_id']
                
        res=super(Book,self).create(val_list)
        return res
    

    
    @api.onchange('name')
    def _find_category(self):
        if self.name:
            self.name = (self.name).upper()
        
        if self.name:
            list=self.name.split(' ')
            print("--------------->",list)
            for i in list:
                company= self.env['sh.library.category'].search([('name', 'ilike', i)])
                if company:
                    print(company)
                    self.cat_id=company.id
    
    
    def unlink(self):
        # print("###############$$$$$$$$$$$$$$$$$$$$$$$")
        for record in self:
            if record.borrow_ids:
                raise ValidationError("This book is borrowed but not returned")
        return super().unlink()
    
    
    # def fun(self):
    #     if self.book_quantity and self.book_quantity >= len(self.member_ids):
    #         self.status='Borrowed'
    #     else:
    #         # self.status='Cart'
    #         raise ValidationError('Quantity is not available')
    
    # def borrow_book(self):
    #     self.fun()


    # def write(self,vals):
    #     vals.fun()
    
    # @api.onchange('')
    # def calculate_quantity(self):
    #     self.book_quantity=self.book_quantity-len(self.member_ids)

            
            
        
        