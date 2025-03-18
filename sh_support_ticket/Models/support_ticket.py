from odoo import fields,models,api,_
from datetime import datetime,timedelta

class Ticket(models.Model):
    _name="support.ticket"
    _description="this models is used to manage the tickets"
    _inherit=['mail.thread','mail.activity.mixin']
    
    # ref=fields.Char("Reference", default=lambda self: _('New'),copy=False, readonly=True)
    name=fields.Char("Name", default=lambda self: _('New'),copy=False, readonly=True)
    developer_id=fields.Many2one('res.users',string="Developer")
    description=fields.Char()
    status=fields.Selection([
        ('draft','Draft'),
        ('active','Active'),
        ('resolve','Resolve'),
        ('close','Close'),
    ],default="draft")

    priority=fields.Selection([
        ('',''),
        ('low','Low'),
        ('medium','Medium'),
        ('high','High')
    ])
    
    support_leader_id=fields.Many2one('res.users',string="Support leader")
    summary=fields.Char()
    
    customer_ticket_id=fields.Many2one('customer.support')
    
    hours=fields.Float()
    
    issue_date=fields.Datetime(default=datetime.now())
    resolve_date=fields.Datetime()
    
    def default_get(self,fields):
        res=super(Ticket,self).default_get(fields)
        res['priority']='low'
        res['status']='draft'

        return res
    
    def ticket_done(self):
        self.status='resolve'
     
    @api.onchange('developer_id')   
    def _available_developer(self):
        if self.developer_id:
            self.status='active'
        else:
            self.status='draft'
            
    def close_ticket(self):
        self.status='close'
        
    def cron_ticket_close(self):
        print(f"\n\n\n\t--------------> 52 ","cron callled")
        print(f"\n\n\n\t--------------> 53 ",self)
        today=datetime.today()
        
        ans=self.env['support.ticket'].search([('resolve_date','<=',today-timedelta(days=7))])
        print(f"\n\n\n\t--------------> 59 ",ans)
        
        ans.write({'status':'close'})
        

    @api.model_create_multi
    def create(self,vals_list):
            for vals in vals_list:
                if vals.get('name', _('New')) == _('New'):
                    vals['name'] = self.env['ir.sequence'].next_by_code('ticket.ticket')
            return super().create(vals_list)
    
    @api.constrains('developer_id')
    def _check_assigned_developer(self):
        ...

