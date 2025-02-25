from odoo import fields,api,models,_
from odoo.exceptions import UserError, ValidationError
from datetime import datetime

class Borrow(models.Model):
    _name="sh.library.borrow"
    _description="this model is used to store data about borrow of library management"
    
    name=fields.Many2one("sh.library.member",string="member")
    borrow_no=fields.Char("Reference", default=lambda self: _('New'),copy=False, readonly=True)
    book_ids=fields.Many2many("sh.library.book",string="Books")
    # book_ids=fields.Many2many("sh.library.borrow",'book_ids',string="borrowed book")
    
    borrow_date=fields.Date(default=datetime.today())
    return_date=fields.Date()
    
    status=fields.Selection([
        ('Cart','cart'),
        ('Borrowed','borrowed'),
        ('Return','Return')
    ],default='Cart')
    
    check=fields.Boolean()
    
    # @api.model_create_multi
    # def create(self,val_list):
    #     for record in val_list:
    #         for i in record['book_ids']:
    #             book=self.env['sh.library.book'].browse(i)
    #             for j in book:
                    
    #                 print("############",j.book_quantity)
    #                 j.book_quantity=j.book_quantity-1
    #         # print("@@@@@@@@@@@@@@@@@@@",record['book_ids'])
            
    #         # self.env['sh.library.member'].create({
    #         #     'borrowed_books':self.book_ids
    #         # })
    #     res= super(Borrow,self).create(val_list)
    #     return res
    
    
    def borrow_book(self):
        not_available_books=[]
        if len(self.book_ids) < 4:
            print(self.check)
            if not self.check:
                for i in self.book_ids:
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!",i)
                    if i.book_quantity>0:
                        i.book_quantity=i.book_quantity-1
                        self.status='Borrowed'
                        print(i.book_quantity)
                        self.check=True
    
                    else:
                        not_available_books.append(i.name)
                if not_available_books:
                    raise ValidationError(f"{not_available_books} book is out of stock!!!!!!")
        else:
            raise ValidationError("selected book limit exceeded")
                
    def return_book(self):
        if self.check:
            for i in self.book_ids:
                i.book_quantity=i.book_quantity+1
                print(i.book_quantity)

                self.check=False
                self.status='Return'


    @api.model_create_multi
    def create(self,val_list):
        for record in val_list:
            print("************************")
            if record.get('borrow_no', _('New')) == _('New'):
                print("+++++++++++++++++++++++++++++",self.env['ir.sequence'].next_by_code('library.borrow'))
                record['borrow_no'] = self.env['ir.sequence'].next_by_code('library.borrow')
        return super(Borrow,self).create(val_list)
        
        
        

                    