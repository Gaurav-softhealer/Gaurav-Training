from odoo import fields,models,api

class PharmacyProduct(models.Model):
    _inherit="product.template"
    
    sh_product_form_id=fields.Many2one('sh.medicine.form',string="Product Form")
    sh_ingredients_id=fields.Many2many('sh.medicine.ingredient',string="Ingredients")
    is_medicine_narcotics=fields.Boolean()
    
    @api.onchange('categ_id')
    def require_product_form(self):
        # if self.categ_id.name=='Narcotics' or self.categ_id.name=='Medicine':
        if self.categ_id.is_medicine==True:
            self.is_medicine_narcotics=True
        else:
            self.is_medicine_narcotics=False


    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'sh_product_form_id' in vals:
                if vals['sh_product_form_id']:
                
                    form_record = self.env['sh.medicine.form'].browse(vals['sh_product_form_id']) 
                    name = vals.get('name')
                    vals['name'] = f"{name} ({form_record.name})"
                else:
                    name = vals.get('name')
                    vals['name'] = f"{name}"

        return super().create(vals_list)


    def write(self, vals):
        if 'sh_product_form_id' in vals:
            form_record = self.env['sh.medicine.form'].browse(vals['sh_product_form_id']) 
            if 'name' in vals:
                name = vals.get('name')
                vals['name'] = f"{name} ({form_record.name})"
            else:
                vals['name']= f"{self.name} ({form_record.name})"

        return super().write(vals)
    
    

class ShProductCategory(models.Model):
    _inherit="product.category"
    
    is_medicine=fields.Boolean()