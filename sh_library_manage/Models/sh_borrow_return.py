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
        
        if len(self.name)==len(ans.book_ids):
            ans.status='Return'
            ans.return_date=datetime.today()


