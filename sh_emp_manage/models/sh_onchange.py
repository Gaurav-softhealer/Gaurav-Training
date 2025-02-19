from odoo import api,fields,models
from datetime import datetime
import re

class Onchange(models.Model):
    _name="sh.onchange"
    _description="this table is used to store the onchange data"
    
    name = fields.Char(string="Name")
    description = fields.Char(string="Description")
    partner_id = fields.Many2one("res.partner", string="Partner")
    
    @api.onchange("partner_id")
    def _onchange_partner_id(self):
        self.name = "Document for %s" % (self.partner_id.name)
        self.description = "Default description for %s" % (self.partner_id.name)
        
        
    birth=fields.Date()
    age=fields.Integer()
    
    @api.onchange('birth')
    def _onchage_birth_age(self):
        if self.birth:
            now=datetime.now()
            current=int(now.strftime("%Y"))
            birth_year=int(self.birth.strftime("%Y"))     
            self.age=current-birth_year
        else:
            self.age=0
            
    
    email=fields.Char(default="a@gmail.com")
    validation_answer=fields.Char()
    
    @api.onchange('email')
    def _validate_email(self):
        valid=re.match("^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,})$",self.email)
        if valid:
            self.validation_answer="email is okk"
        else:
            self.validation_answer="not okkk"    