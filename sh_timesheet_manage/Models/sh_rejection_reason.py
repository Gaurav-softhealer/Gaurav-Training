from odoo import models,fields
from datetime import datetime

class Tag(models.TransientModel):
    _name="sh.rejection.reason"
    _description="this model is used to store information about the rejection reason"
    
    name=fields.Char()
    
    def reject_button(self):
        active_id=self.env.context.get('active_ids')
        active_model=self.env.context.get('active_model')

        rec=self.env[active_model].browse(active_id)
        
        print("###############",rec)
        
        rec.rejection_reason=self.name
        rec.rejected_by=self.env.uid
        rec.rejection_time=datetime.today()
        rec.state='reject'

    
    