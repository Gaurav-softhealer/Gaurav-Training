from odoo import models,fields,api,Command
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = ['sale.order']
    
    sale_workflow = fields.Many2one(related="company_id.sh_default_workflow",string="Sale Workflow",readonly=False)
    sh_enable = fields.Boolean(related="company_id.sh_enable",string="Enable")
    

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        for rec in self:
            if rec.partner_id.sale_workflow:
                rec.sale_workflow = rec.partner_id.sale_workflow.id
            else:
                rec.sale_workflow = rec.company_id.sh_default_workflow.id

    
    def action_confirm(self):
        
        res = super().action_confirm()
            
        for rec in self:
        
            #THIS IS FOR DELIVERY (stock.picking)
            if rec.sh_enable:

                if rec.sale_workflow.delivery_order == True:
                    for product in rec.picking_ids.move_ids_without_package:
                        product.quantity = product.product_uom_qty
                
                
                    #THIS VALIDATES THE DELIVERY AND MOVES THIS DELIVERY TO DONE STAGE
                    if rec.sale_workflow.force_transfer == True:
                        
                        rec.picking_ids.with_context(skip_sms=True).button_validate()
                
                #===========
            
                #THIS CREATES THE INVOICE OF THE CONFIRMED ORDER
                if rec.sale_workflow.create_invoice == True:
                    invoice = self._create_invoices()
                    
                    if rec.sale_workflow.validate_invoice == True:
                        invoice.action_post()
                

                        #THIS IS TO MAKE THE PAID INVOICE
                        if rec.sale_workflow.register_payment == True:
                            action = invoice.action_register_payment()
                
                            ctx = action['context']
                            
                            ctx.update({
                                'active_model': 'account.move.line',
                                'active_ids': rec.invoice_ids.line_ids.ids,
                                'default_journal_id': rec.sale_workflow.payment_journal.id,
                                'default_payment_method_line_id':rec.sale_workflow.payment_method.id,
                            })
                            
                            invoice.action_force_register_payment()  
                            wizard = self.env['account.payment.register'].with_context(ctx).create({})
                            
                            wizard.action_create_payments()
                            # self.invoice_ids.matched_payment_ids.action_validate()

                        #THIS IS FOR AUTOMATIC EMAIL
                        if rec.sale_workflow.send_invoice_by_email == True:
                            
                            act = invoice.action_invoice_sent()
                            
                            ctx2 = act['context']
                            
                            ctx2.update({
                                'active_model': 'account.move',
                                'active_ids': rec.invoice_ids.ids
                            })
                            
                            wiz = self.env['account.move.send.wizard'].with_context(ctx2).create({})
                            wiz.action_send_and_print()

            
        return res