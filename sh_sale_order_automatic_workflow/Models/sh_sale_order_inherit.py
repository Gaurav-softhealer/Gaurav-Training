from odoo import fields,models,api
from datetime import datetime

class SaleOrder(models.Model):
    _inherit="sale.order"
    
    sh_work_id = fields.Many2one('sh.sale.auto.workflow',string="Auto Workflow")

    @api.onchange('partner_id')
    def _set_workflow_value(self):
        a=self.env['res.partner'].browse(self.partner_id.id)
        print(a)
        print(f"\n\n\n\t--------------> 16 ",self.partner_id.company_id.sh_default_workflow.id)
        if self.partner_id.workflow_id:
            self.sh_work_id=a.workflow_id
        else:
            self.sh_work_id=self.company_id.sh_default_workflow.id

    
    def action_confirm(self):
        res=super().action_confirm()

        print(f"\n\n\n\t--------------> 11 ",self)
        print(f"\n\n\n\t--------------> 13 ",self.sh_work_id.delivery_order)
        
        if self.sh_work_id.delivery_order:
            ans=self.env['stock.picking'].search([('origin','=',self.name)])
            ans.button_validate()
        
        if self.sh_work_id.create_invoice:
            self._create_invoices()
            
            if self.sh_work_id.validate_invoice:
                result=self.env['account.move'].search([('invoice_origin','=',self.name)])
                result.action_post()
            
                if self.sh_work_id.register_payment:
                        self.env["account.payment.register"].with_context(
                                active_model="account.move",
                                active_ids=result.ids,
                                payment_method_line_id = self.sh_work_id.payment_method.id,
                                journal_id = self.sh_work_id.sh_payment_journal.id).create({"group_payment": False}).action_create_payments()
 
                        # answer=self.env['account.payment'].search([('memo','=',self.order_line.invoice_lines.move_id.name)])
                        # print(answer)
                        
                if self.sh_work_id.send_email:
                    self.env['account.move.send.wizard'].create({"move_id":result.id}).action_send_and_print() 

        return res
    
    
    class ShPayment(models.Model):
        _inherit="account.payment"
        @api.model_create_multi
        def create(self, vals_list):
            print(vals_list)
            return super().create(vals_list)
