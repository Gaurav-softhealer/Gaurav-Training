from odoo import fields,models

class CustomerSupport(models.Model):
    _name="customer.support"
    _description="model about the customer"
    
    name=fields.Many2one('res.users',string="Customer")
    
    def default_get(self,fields):
        res=super(CustomerSupport,self).default_get(fields)
        res['name']=self.env.uid

        return res
    
    ticket_ids=fields.One2many('support.ticket','customer_ticket_id')
    
    def open_ticket_form(self):
        print(f"\n\n\n\t--------------> 10 ","smart button called")
        # print(f"\n\n\n\t--------------> 11 ",self.env.context)
        res=self.env['support.ticket'].search([('developer_id','=',self.id)])
        print(f"\n\n\n\t--------------> 13 ",res)
        return {
            'type': 'ir.actions.act_window',
            'name': 'Name of window',
            'view_mode': 'list',
            'res_model': 'support.ticket',
            'domain': [('id', '=', self.ticket_ids.ids)],  
           
        }
