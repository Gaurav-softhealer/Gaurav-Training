from odoo import fields,models,api

class CustomerSupport(models.Model):
    _name="customer.support"
    _description="model about the customer"
    
    name=fields.Many2one('res.partner',string="Customer")
    
    # def default_get(self,fields):
    #     res=super(CustomerSupport,self).default_get(fields)
    #     res['name']=self.env.uid

    #     return res
    
    ticket_ids=fields.One2many('support.ticket','customer_ticket_id')
    
    def open_ticket_form(self):
        print(f"\n\n\n\t--------------> 10 ","smart button called")
        # print(f"\n\n\n\t--------------> 11 ",self.env.context)
        res=self.env['support.ticket'].search([('developer_id','=',self.id)])
        print(f"\n\n\n\t--------------> 13 ",res)
        
        print(f"\n\n\n\t--------------> 23 ",self.total_record)
        if self.total_record==1:
            return {
            'type': 'ir.actions.act_window',
            'name': 'Name of window',
            'view_mode': 'form',
            'res_model': 'support.ticket',
            'domain': [('id', '=', self.ticket_ids)],  
           
        }
        else:
            return {
                'type': 'ir.actions.act_window',
                'name': 'Name of window',
                'view_mode': 'list,form',
                'res_model': 'support.ticket',
                'domain': [('id', 'in', self.ticket_ids.ids)],  
            
            }
            
    total_record=fields.Integer(compute="count_record")
    
    @api.depends('ticket_ids')
    def count_record(self):
        for i in self:
            i.total_record=len(i.ticket_ids)
        print(f"\n\n\n\t--------------> 37 ",self.total_record)
        
        
    class Invoice(models.Model):
        _inherit="account.move"
    
        data=fields.Char()
        def open_support_ticket(self):
            print(f"\n\n\n\t--------------> 92 ","my function called")
            return{
                'type': 'ir.actions.act_window',
                'name': 'Name of window',
                'view_mode': 'form',
                'res_model': 'support.ticket',
                'target':'new',
                'context':{
                    'default_name':self.id,
                    'default_customer_id':self.partner_id.id
                    # 'default_developer_id':self.partner_id.id
                }
                # 'res_id':3,
            }
        
        
