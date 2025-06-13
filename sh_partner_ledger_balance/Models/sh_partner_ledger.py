from collections import defaultdict
from odoo import fields, models

class ShPartnerLedgerWizard(models.TransientModel):
    _name = 'sh.partner.ledger.wizard'
    _description = "Partner Ledger Wizard"

    sh_target_moves = fields.Selection([
        ('posted', 'All Posted Entries'),
        ('all', 'All Entries')
    ], string="Target Moves", default='posted')

    sh_initial_balance = fields.Boolean(string="Show Initial Balance")
    sh_closing_balance = fields.Boolean(string="Show Closing Balance")
    sh_reconsile_entry = fields.Boolean(string="Include Reconciled Entries")
    sh_start_date = fields.Date(string="Start Date")
    sh_end_date = fields.Date(string="End Date")
    sh_payable_type = fields.Selection([
        ('receivable', 'Receivable Accounts'),
        ('receive_pay', 'Receivable and Payable Accounts')
    ], string="Partner's")
    sh_company_id=fields.Many2one('res.company',default=lambda self: self.env.company)
    sh_partner_ids = fields.Many2many('res.partner', string="Partners")
    sh_journals_ids = fields.Many2many('account.journal', string="Journals")

    def partner_ledger_print(self):
        # print(f"\n\n\n\t--------------> 25 ","Print button called")
        
        # if self.sh_start_date:
        #     records=self.env['account.move.line'].search([('date','>=',self.sh_start_date)])
        # else:
        #     records=self.env['account.move.line'].search([])
        # print(f"\n\n\n\t--------------> 28 records",records)
        # data = {
        #         'records': records,
        #         }
        # print(f"\n\n\n\t--------------> 35 data",data)
        return self.env.ref('sh_partner_ledger_balance.print_partner_ledger_report_action').report_action(self)
        



class ReportPartnerLedger(models.AbstractModel):
    _name = 'report.sh_partner_ledger_balance.print_partner_ledger_report'
    _description = 'Partner Ledger Report'

    def _get_report_values(self, docids, data=None):
        wizard = self.env['sh.partner.ledger.wizard'].browse(docids)

        domain = []
        if wizard.sh_start_date:
            domain.append(('date', '>=', wizard.sh_start_date))
        if wizard.sh_end_date:
            domain.append(('date', '<=', wizard.sh_end_date))
        if wizard.sh_journals_ids:
            domain.append(('journal_id', 'in', wizard.sh_journals_ids.ids))
        if wizard.sh_partner_ids:
            domain.append(('partner_id', 'in', wizard.sh_partner_ids.ids))

        # Get filtered move lines for display
        all_lines = self.env['account.move.line'].search(domain, order='partner_id, date')

        # Group move lines by partner_id
        grouped_records = defaultdict(lambda: self.env['account.move.line'])
        for line in all_lines:
            if line.partner_id:
                grouped_records[line.partner_id.id] += line

        # Compute ONLY ONE initial balance per partner (BEFORE sh_start_date)
        initial_balances = {}
        for partner_id in grouped_records:
            init_domain = [('partner_id', '=', partner_id)]
            if wizard.sh_start_date:
                init_domain.append(('date', '<=', wizard.sh_start_date))
            if wizard.sh_journals_ids:
                init_domain.append(('journal_id', 'in', wizard.sh_journals_ids.ids))

            init_lines = self.env['account.move.line'].search(init_domain)
            init_debit = sum(init_lines.mapped('debit'))
            init_credit = sum(init_lines.mapped('credit'))
            init_balance = sum(init_lines.mapped('balance'))

            initial_balances[partner_id] = {
                'debit': init_debit,
                'credit': init_credit,
                'balance': init_balance,
            }


        partners = self.env['res.partner'].browse(grouped_records.keys())

        return {
            'doc_ids': docids,
            'doc_model': 'sh.partner.ledger.wizard',
            'docs': wizard,
            'partners': partners,
            'grouped_records': grouped_records,
            'initial_balances': initial_balances,  # {partner_id: {debit, credit, balance}}
            'sh_start_date': wizard.sh_start_date,
            'sh_end_date': wizard.sh_end_date,
            'company': wizard.sh_company_id or self.env.company,
        }
