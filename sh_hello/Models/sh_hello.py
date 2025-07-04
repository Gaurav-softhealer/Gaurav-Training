from odoo import fields,models

class Hello(models.MOdel):
    _name="sh.hello"
    _description="this is demo module"

    name=fields.Char()