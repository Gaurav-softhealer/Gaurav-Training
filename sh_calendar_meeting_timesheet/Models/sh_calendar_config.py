from odoo import fields,models,api

class SaleConfig(models.TransientModel):
    _inherit="res.config.settings"
    
    group_create_calendar=fields.Boolean(string="create calendar",related='company_id.create_calendar',implied_group="sh_calendar_meeting_timesheet.sh_calendar_timesheet_groups",readonly=False)

class ResCompany(models.Model):
    _inherit="res.company"
    
    create_calendar=fields.Boolean()

