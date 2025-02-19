from odoo import fields,models,api
from odoo.exceptions import UserError, ValidationError
import random

class Category(models.Model):
    _name="sh.library.category"
    _description="this model is used to store data about book in library"
    
    name=fields.Char()
    cat_description=fields.Char(string="Description")
    book_ids=fields.One2many('sh.library.book','cat_id',string="book data")
    count=fields.Integer(compute="_count_books")
    
    @api.depends('book_ids')
    def _count_books(self):
        for record in self:
            record.count=len(record.book_ids)

    def unlink(self):
        for record in self:
            if record.book_ids:
                raise ValidationError("Book exist inside this category")
        return super().unlink()