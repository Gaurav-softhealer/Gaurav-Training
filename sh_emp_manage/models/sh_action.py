from odoo import fields,api,models

class Action(models.Model):
    _name="sh.action"
    _description="this table is used to store data about actions"
    
    name=fields.Char()
    
    def accept_button(self):
        for record in self:
            record.name="accept"
            
            
    def reject_button(self):
        for record in self:
            record.name="reject"
            
            