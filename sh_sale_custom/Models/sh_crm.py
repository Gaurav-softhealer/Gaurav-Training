from odoo import fields,models,api

class ShCrm(models.Model):
    _inherit="crm.lead"
    
    text=fields.Char(string="Text")
    
    
class Employeeee(models.Model):
    _inherit="res.partner"
    
    partner=fields.Many2one("sh.employee.new")
    department_id=fields.Char()
    
    @api.onchange('partner')
    def _find_partner(self):
        print("#################################",self.partner)
        # ans=self.env['sh.employee.new'].browse(self.partner)
        # print("*********************************",ans)
        # self.department_id=self.partner.
        