from odoo import fields,models,api

class PharmacyProduct(models.Model):
    _inherit="product.template"
    
    sh_product_form_id=fields.Many2one('sh.medicine.form',string="Product Form")
    sh_ingredients_id=fields.Many2many('sh.medicine.ingredient',string="Ingredients")
    is_medicine_narcotics=fields.Boolean()
    
    @api.onchange('categ_id')
    def require_product_form(self):

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
 
    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        args = args or []
        if name:
            new_domain = [
                '|',
                ('name', operator, name),
                 ('sh_ingredients_id.name', operator, name),
            ]
            domain = new_domain + args
        else:
            domain = args
        records = self.search_fetch(domain, ['display_name'], limit=limit)
        list_product =  [(record.id, record.display_name) for record in records.sudo()]
        res = super().name_search(
            name=name, args=domain, operator=operator, limit=limit)
        res+=list_product
        return res


class ShProductCategory(models.Model):
    _inherit="product.category"
    
    is_medicine=fields.Boolean()
    is_narcotics=fields.Boolean()