from odoo import api,models,fields

class Test(models.Model):
    _name="sh.test"
    _description="this table is only for testing purpose"
    
    # dep_id=fields.Many2one("sh.department")
    # parent_id=fields.Char(compute="_find_parent")
    
    # @api.depends('dep_id')
    # def _find_parent(self):
    #     for record in self:
    #         record.parent_id=record.dep_id.parent_dep_id.name
            
            
    dep_id=fields.Many2one("sh.department")
    job_ids=fields.One2many("sh.job", compute="_find_jobs")
    
    @api.depends('dep_id')
    def _find_jobs(self):
        for record in self:
            record.job_ids=record.dep_id.job_ids
    
           