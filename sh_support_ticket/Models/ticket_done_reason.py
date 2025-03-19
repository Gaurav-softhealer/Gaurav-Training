from odoo import fields,models
from datetime import datetime

class Ticket(models.TransientModel):
    _name="ticket.done.reason"
    _description="this models is used to manage the tickets done reasons"
    
    name=fields.Char()
    developer_id=fields.Many2one('res.users',string="Developer")
    support_leader_id=fields.Many2one('res.users',string="Support leader")
    summary=fields.Char(string="Summary")
    resolve_date=fields.Datetime(default=datetime.now())
    
    def default_get(self, fields_list):
        active_id=self.env.context.get('active_ids')
        active_model=self.env.context.get('active_model')
        res=super().default_get(fields_list)
        
        ans=self.env[active_model].browse(active_id)
        
        # res['name']=ans.name
        # res['developer_id']=ans.developer_id
        # res['support_leader_id']=ans.support_leader_id

        return res
    
    def resolve_ticket(self):
        print(f"\n\n\n\t--------------> 26 ",)
        active_id=self.env.context.get('active_ids')
        active_model=self.env.context.get('active_model')

        ans=self.env[active_model].browse(active_id)
        
        ans.status='resolve'
        ans.summary=self.summary
        ans.resolve_date=self.resolve_date