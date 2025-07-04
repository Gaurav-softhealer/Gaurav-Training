from odoo import fields,models,api
from datetime import datetime

class ShPartners(models.Model):
    _inherit="res.partner"

    sh_first_visit=fields.Date(string="First Visit")
    sh_next_visit=fields.Date(string="Next Visit")
    scheduled_date=fields.Integer(string="Scheduled Date")
    sh_sale_team=fields.Many2one('crm.team',string="Sale Team")
    sh_location=fields.Char(string="Location")

    sh_visit_count=fields.Integer(string="Sale Visit",compute="_compute_visit_record")

    def sale_visit(self):

        partner_records=self.env['res.partner'].search([('sh_next_visit','=',datetime.today())])

        for record in partner_records:
            self.env['sh.sale.visit'].create(
                {
                    'sh_customer_id':record.id,
                    'sh_location':record.sh_location,
                    'sh_visit_date':datetime.today(),
                    'sh_salesperson_id':record.user_id.id,
                    'sh_phone':record.phone,
                    'sh_mobile':record.mobile,                   
                }
            )
            record.scheduled_date+=1

    def action_customer_visit(self):
        return {
            'view_mode': 'list,form',
            'name': 'customer_visit_record',
            'res_model': 'sh.sale.visit',
            'type': 'ir.actions.act_window',
            'domain':[('sh_customer_id','=',self.id)]
        }

    def _compute_visit_record(self):
        for record in self:
            record.sh_visit_count=self.env['sh.sale.visit'].search_count([('sh_customer_id','=',record.id)])
