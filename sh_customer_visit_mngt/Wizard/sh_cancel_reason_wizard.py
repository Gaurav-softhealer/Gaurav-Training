from odoo import fields,models,api

class CancelReasonWizard(models.TransientModel):
    _name='sh.cancel.reason.wizard'
    _description='This model is for cancel reason wizard'

    name=fields.Many2one('sh.cancel.reason',string="Cancel Reason")
    sh_notes=fields.Char(string="Notes")

    def confirm_cancel_reason(self):
        
        active_id=self.env.context.get('active_id')
        active_model=self.env.context.get('active_model')

        wizard_record=self.env[active_model].browse(active_id)

        wizard_record.sh_cancel_reason=self.name.id
        wizard_record.sh_notes=self.sh_notes
        wizard_record.sh_status='cancel'
