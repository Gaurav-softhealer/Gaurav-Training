from odoo import fields,models

class BorrowReturn(models.TransientModel):
    _name="sh.borrow.return"
    _description="this model is to manage return order of the books"
    
    # book_ids=fields.Many2many("sh.library.borrow")
    
    def return_book(self):
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        active_id=self.env.context.get('active_ids')
        active_model=self.env.context.get('active_model')
        
        ans=self.env[active_model].browse(active_id)
        print("------------------------------------>",ans.book_ids)
        
        # try with for loop on ans.book_ids
        

