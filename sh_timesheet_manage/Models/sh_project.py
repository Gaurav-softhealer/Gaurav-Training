from odoo import fields,models,api

class Project(models.Model):
    _name="sh.project"
    _description="this model is used to store data about the project"
    
    name=fields.Char(string="project name")