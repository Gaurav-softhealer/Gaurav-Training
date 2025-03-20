from odoo import fields,models,api,_
from datetime import datetime,timedelta
from odoo.exceptions import UserError, ValidationError

class Ticket(models.Model):
    _name="support.ticket"
    _description="this models is used to manage the tickets"
    _inherit=['mail.thread','mail.activity.mixin']
    
    def get_only_dev_domain(self):
        users_list = []
        rec_users = self.env["res.users"].search([])
        for rec in rec_users:
            # users_list.append(rec.id)
            # print(f"\n\n\n\t--------------> 15 ",rec.id)
            if rec.has_group("sh_support_ticket.support_ticket_group_developer"):
                users_list.append(rec.id)
        # print("\n\n\n\n",users_list)
        return [('id','in',users_list)]
        # return [(1,'=',1)]

    
    ref=fields.Char("Reference", default=lambda self: _('New'),copy=False, readonly=True)
    name=fields.Many2one('account.move',string="Invoice")
    developer_id=fields.Many2one('res.users',string="Developer",domain=get_only_dev_domain)
    # dev_id=fields.Many2one('res.partner')
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
    
    customer_id=fields.Many2one('res.partner')
    
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
        
    def close_ticket_wizard(self):
        print(f"\n\n\n\t--------------> 62 ",)
        return {
            'type': 'ir.actions.act_window',
            'name': 'Resolve Ticket Wizard',
            'view_mode': 'form',
            'res_model': 'ticket.done.reason',
            'target': 'new',
        }

        
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
                if vals.get('ref', _('New')) == _('New'):
                    vals['ref'] = self.env['ir.sequence'].next_by_code('ticket.ticket')
            res= super().create(vals_list)
            
            rec_customer_support =self.env["customer.support"].search([('name','=',res.customer_id.id)])
            if rec_customer_support:
                    rec_customer_support.write({"ticket_ids": [(4,res.id,0)]})
            else:
                self.env["customer.support"].create([{'name':res.customer_id.id,'ticket_ids': [(4,res.id,0)]}])
            return res
            
    
    @api.constrains('developer_id')
    def _check_assigned_developer(self):
        ans=self.env['support.ticket'].search([('developer_id','=',self.developer_id.id),('status','=','active'),("id","!=",self.id)])
        if ans:
            raise ValidationError('Developer already assigned')
            
        # if len(ans)>1:
        # print(f"\n\n\n\t--------------> 82 ",len(ans))
        #     raise ValidationError('Developer already assigned')
       
       
    def open_invoice_form(self):
        print(f"\n\n\n\t--------------> 88 ","invoice button called")
        return{
            'type': 'ir.actions.act_window',
            'name': 'Invoice Ticket',
            'view_mode': 'form',
            'res_model': 'account.move',
            'res_id':self.name.id,
            # 'target': 'new',
        }
        
    