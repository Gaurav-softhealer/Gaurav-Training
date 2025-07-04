from odoo import fields, models, api, _
from datetime import datetime

class SaleVisit(models.Model):
    _name = "sh.sale.visit"
    _description = "This model is used to store data about sales visits"

    name = fields.Char(default=lambda self: _('New'), readonly=True, copy=False, help="Reference Number of the book")
    sh_customer_id = fields.Many2one('res.partner', string="Customer",readonly=True)
    sh_location = fields.Char(string="Location",readonly=True)
    sh_phone = fields.Char(string="Phone",readonly=True)
    sh_mobile = fields.Char(string="Mobile",readonly=True)
    sh_salesperson_id = fields.Many2one('res.users', string="Salesperson",readonly=True)
    is_buy = fields.Boolean(string="Is Buy?")
    sh_visit_date = fields.Date(string="Visit Date",readonly=True)
    sh_start_date = fields.Date(string="Start Date",readonly=True)
    sh_end_date = fields.Date(string="End Date",readonly=True)
    sh_status=fields.Selection([
        ('draft','Draft'),
        ('process','In Process'),
        ('done','Done'),
        ('cancel','Cancel')
    ],default='draft')

    sh_cancel_reason=fields.Many2one('sh.cancel.reason',string="Cancel Reason",readonly=True)
    sh_notes=fields.Char("Notes",readonly=True)

    sh_order_count=fields.Integer(compute="_count_sale_order")


    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('customer.visit') or _('New')
        return super(SaleVisit, self).create(vals_list)

    def cancel_customer_visit(self):

        return {
            'view_mode': 'form',
            'name': 'cancel_reason_wizard',
            'res_model': 'sh.cancel.reason.wizard',
            'type': 'ir.actions.act_window',
            'target':'new'
        }

    def start_customer_visit(self):
        self.sh_start_date=datetime.today()
        self.sh_status='process'
        
    def done_customer_visit(self):
        self.sh_end_date=datetime.today()
        self.sh_status='done'

    def new_quotation(self):
        return{
            'view_mode': 'form',
            'name': 'new_quotation',
            'res_model': 'sale.order',
            'type': 'ir.actions.act_window',
            'context':{'default_partner_id':self.sh_customer_id.id,
                        'default_user_id':self.sh_salesperson_id.id,
            }
        }

    def action_sale_order(self):
        return{
            'view_mode': 'list',
            'name': 'customer_visit_record',
            'res_model': 'sale.order',
            'type': 'ir.actions.act_window',
            'domain':[('partner_id','=',self.sh_customer_id.id),('user_id','=',self.sh_salesperson_id.id)]
        }
        
    def _count_sale_order(self):
        for record in self:
            record.sh_order_count=self.env['sale.order'].search_count([('partner_id','=',self.sh_customer_id.id),('user_id','=',self.sh_salesperson_id.id)])
        