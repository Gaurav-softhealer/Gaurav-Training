from odoo import fields,models
from datetime import datetime

class BorrowReturn(models.TransientModel):
    _name="sh.borrow.return"
    _description="this model is to manage return order of the books"
    
    lst=[]
    def get_all_data(self):
        active_id=self.env.context.get('active_ids')
        active_model=self.env.context.get('active_model')
        print("#################################################",self.env.context)
        ans=self.env[active_model].browse(active_id)
        print("***********************",ans)
        
        final=self.env['sh.library.book'].search([('id','in',ans.book_ids.ids)])
        print("+++++++++++++++++++++++++++",final)
        return final
        # return ans.book_ids
    
    name=fields.Many2many('sh.library.book',default=get_all_data)
    # def default_get(self, fields):
    #     res=super().default_get(fields)
    #     ans=self.get_all_data()
    #     res.update({ans.book_ids.name})
        # print("------------------------------------>",ans.book_ids)
        
        # try with for loop on ans.book_ids
        # for i in ans.book_ids:
        #     self.lst.append(i.name)
        # print("###################3",self.lst)
    
    def return_book(self):
        
        active_id=self.env.context.get('active_ids')
        active_model=self.env.context.get('active_model')
        
        ans=self.env[active_model].browse(active_id)
        
        for i in ans.book_ids:
            print("####################",i.name)
            print("########################",i.book_quantity)
            i.book_quantity+=1
            print("####################",i.name)
            print("########################",i.book_quantity)
        
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        
        ans.status='Return'
        ans.return_date=datetime.today()
        
        
        # active_id=self.env.context.get('active_ids')
        # active_model=self.env.context.get('active_model')
        
        # ans=self.env[active_model].browse(active_id)
        # print("------------------------------------>",ans.book_ids)
        
        # # try with for loop on ans.book_ids
        # for i in ans.book_ids:
        #     self.lst.append(i.name)
        # print("###################3",self.lst)
        #     # self.book_ref_ids=i.name

