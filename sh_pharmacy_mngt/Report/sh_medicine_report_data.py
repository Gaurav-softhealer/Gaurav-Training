from odoo import fields,models,api

class ShMedicineReport(models.Model):
    _name = "sh.medicine.report"
    _description = "Medicine Report"

    product_id = fields.Many2one("product.product")
    category_id = fields.Many2one("product.category")
    sold_qty = fields.Float()
    unit_price = fields.Float()
    total_sale = fields.Float()