from odoo import fields, models,api
from odoo.exceptions import ValidationError

class AttributeProduct(models.TransientModel):
   _name = 'attribute.product'
   _description = "Attribute Product"

   variant_product = fields.Many2one('product.template',string="Product Variant")
   attribute= fields.Many2one('product.attribute',string="Attribute")
   values = fields.Many2one('product.attribute.value',string="Values", domain="[('attribute_id', '=', attribute)]")
   
   def make_product_as_variant(self):      
      count=0
      product_ids = self.env.context.get('active_ids', [])
      product_rec = self.env['product.template'].browse(product_ids)
      if self.variant_product != product_rec:
         x = self.attribute
         for line in product_rec.attribute_line_ids:
            if line.attribute_id == x:
               line.write({'value_ids': [(4, self.values.id)]})
               count=1
         if count==0:
            self.env['product.template.attribute.line'].create({
               'attribute_id': x.id,
               'value_ids': [(6, 0, [self.values.id])],
               'product_tmpl_id': product_rec.id,
               })
         locations = self.env['stock.warehouse'].search([]).mapped('lot_stock_id')
         for loc in locations:
            stock = self.env['stock.quant'].search([
              ('product_tmpl_id', '=', self.variant_product.id),
              ('location_id', '=', loc.id)
            ])
            self.env['stock.quant'].create({
               'product_id': product_rec.product_variant_ids[-1].id,
               'location_id': loc.id,
               'quantity': int(sum(stock.mapped('quantity'))),
            })
         barcode = self.variant_product.barcode
         default_code = self.variant_product.default_code
         self.variant_product.default_code = False
         self.variant_product.barcode = False
         product_rec.product_variant_ids[-1].barcode = barcode
         product_rec.product_variant_ids[-1].default_code = default_code
         self.variant_product.write({'active': False})      
      else:
         raise ValidationError('Can not merge same product template.')

