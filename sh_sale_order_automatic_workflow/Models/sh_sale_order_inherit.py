from odoo import fields,models,api

class SaleOrder(models.Model):
    _inherit="sale.order"
    
    workflow_id=fields.Many2one('sh.sale.auto.workflow',string="Sale Workflow")
    
    def action_confirm(self):
        res=super().action_confirm()

        print(f"\n\n\n\t--------------> 11 ",self)
        print(f"\n\n\n\t--------------> 13 ",self.workflow_id.delivery_order)
        
        if self.workflow_id.delivery_order:
            ans=self.env['stock.picking'].search([('origin','=',self.name)])
            ans.button_validate()
            # print(f"\n\n\n\t--------------> 16 ",ans)
        
        if self.workflow_id.create_invoice:
            
                
        return res
    
    