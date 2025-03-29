from odoo import fields,models,api
from datetime import datetime

class SaleOrder(models.Model):
    _inherit="sale.order"
    
    sh_work_id = fields.Many2one('sh.sale.auto.workflow',string="6767")
    # sh_company_id=fields.Many2one('res.company',default=lambda self: self.env.company)
    @api.onchange('partner_id')
    def _set_workflow_value(self):
        a=self.env['res.partner'].browse(self.partner_id.id)
        print(a)
        print(f"\n\n\n\t--------------> 16 ",self.partner_id.company_id.sh_default_workflow.id)
        if self.partner_id:
            self.sh_work_id=a.workflow_id
        else:
            # self.sh_work_id=self.env.company.sh_default_workflow.id
            self.sh_work_id=self.company_id.sh_default_workflow.id

    
    def action_confirm(self):
        res=super().action_confirm()

        print(f"\n\n\n\t--------------> 11 ",self)
        print(f"\n\n\n\t--------------> 13 ",self.sh_work_id.delivery_order)
        
        if self.sh_work_id.delivery_order:
            ans=self.env['stock.picking'].search([('origin','=',self.name)])
            ans.button_validate()
            # print(f"\n\n\n\t--------------> 16 ",ans)
        
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
 
                        answer=self.env['account.payment'].search([('memo','=',self.order_line.invoice_lines.move_id.name)])
                        print(answer)
                        
                        # answer.action_validate()
                    
                    
                    
                    # answer=self.env['payment.method'].search([])
                    # for i in answer:
                    #     print(f"\n\n\n\t--------------> 29 ",i.id)
                    # print(f"\n\n\n\t--------------> 28 ",answer)
                    # print(f"\n\n\n\t--------------> 27 ",self)
                    # print(f"\n\n\n\t--------------> 33 ",self.order_line.invoice_lines.move_id.name)
                    # self.env['account.payment'].create({
                    #     'payment_type':'inbound',
                    #     'partner_id':self.partner_id.id,
                    #     'journal_id':1,
                    #     'memo':result.name,
                    #     'amount':result.amount_residual,
                    #     'date':datetime.today(),
                    #     'payment_method_line_id': 1,
                    #     'journal_id': 6,
                    #     'company_id': 1,
                    #     'currency_id': 1,
                    #     'invoice_ids':[result.id]
                        
                        
                    # })
                    
                    # print(f"\n\n\n\t--------------> 48 ",self.name)
                    # answer=self.env['account.payment'].search([('memo','=',self.order_line.invoice_lines.move_id.name)])
                    # print(answer)
                    
                    # answer.action_validate()
                    # result.amount_residual=0
                    
                    
                    # self.order_line.invoice_lines.reconcile()
                    
                    # result._action_create_payments()
                    # result._compute_payments_widget_reconciled_info()
                    
                    # print(f"\n\n\n\t--------------> 56 ",result.payment_state)
                    # result.payment_state='paid'
                    # print(f"\n\n\n\t--------------> 57 ",result.payment_state)
                    # result.move_type='out_invoice'
                    
                    # self.env['account.move'].write({
                    #     'payment_state':'paid'
                    # })
                    # print(f"\n\n\n\t--------------> 57 ",result.payment_state)

                    
                    # result.button_open_invoices()
                    # result.button_open_bills()
                    # result.button_open_statement_lines()   
                    # answer.button_open_journal_entry()                 
                

        return res
    
    
    class ShPayment(models.Model):
        _inherit="account.payment"
        @api.model_create_multi
        def create(self, vals_list):
            print(vals_list)
            return super().create(vals_list)
    
    # reconciled_invoice_ids
    # reconciled_bill_ids