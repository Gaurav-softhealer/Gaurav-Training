from odoo import fields,models,api

class ShCancelReason(models.Model):
    _name='sh.cancel.reason'
    _description="This model is used to store information about Cancel Reason"

    name=fields.Char(string="Cancel Reason")