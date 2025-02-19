from odoo import api,fields,models

class Trip(models.Model):
    _name="sh.trip"
    _description="this table is used to store data about trip student"
    
    user_name=fields.Many2one('sh.employee')
    # name=fields.Char()
    image=fields.Binary()
    
    @api.onchange('user_name')
    def _image_get(self):
        self.image=self.user_name.file
        
        

                    