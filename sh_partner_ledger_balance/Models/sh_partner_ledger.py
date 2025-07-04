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
    sh_company_id = fields.Many2one('res.company', default=lambda self: self.env.company)
    sh_partner_ids = fields.Many2many('res.partner', string="Partners")
    sh_journals_ids = fields.Many2many('account.journal', string="Journals")

    def partner_ledger_print(self):
        return self.env.ref('sh_partner_ledger_balance.print_partner_ledger_report_action').report_action(self)


class ReportPartnerLedger(models.AbstractModel):
    _name = 'report.sh_partner_ledger_balance.print_partner_ledger_report'
    _description = 'Partner Ledger Report'

    def _get_report_values(self, docids, data=None):
        wizard = self.env['sh.partner.ledger.wizard'].browse(docids)

        base_domain = []
        if wizard.sh_target_moves=='posted':
            base_domain.append(('move_id.state', '=', 'posted'))
        if wizard.sh_target_moves=='all':
            base_domain.append(('move_id.state','in',['draft','posted','cancel']))
        if wizard.sh_reconsile_entry:
            base_domain.append(('account_id.reconcile', '=', True))
        if wizard.sh_journals_ids:
            base_domain.append(('journal_id', 'in', wizard.sh_journals_ids.ids))
        if wizard.sh_partner_ids:
            base_domain.append(('partner_id', 'in', wizard.sh_partner_ids.ids))
        if wizard.sh_payable_type == 'receivable':
            base_domain.append(('account_id.account_type', '=', 'asset_receivable'))
        elif wizard.sh_payable_type == 'receive_pay':
            base_domain.append(('account_id.account_type', 'in', ['asset_receivable', 'liability_payable']))

        initial_domain = base_domain.copy()
        if wizard.sh_start_date:
            initial_domain.append(('date', '<', wizard.sh_start_date))
        initial_lines = self.env['account.move.line'].search(initial_domain)

        initial_balances = defaultdict(lambda: {'credit': 0.0, 'debit': 0.0, 'balance': 0.0})
        for line in initial_lines:
            if line.partner_id:
                pid = line.partner_id.id
                initial_balances[pid]['credit'] += line.credit
                initial_balances[pid]['debit'] += line.debit
                initial_balances[pid]['balance'] += line.balance

        current_domain = base_domain.copy()
        if wizard.sh_start_date:
            current_domain.append(('date', '>=', wizard.sh_start_date))
        if wizard.sh_end_date:
            current_domain.append(('date', '<=', wizard.sh_end_date))
        current_lines = self.env['account.move.line'].search(current_domain, order='partner_id, date')

        grouped_records = defaultdict(lambda: self.env['account.move.line'])
        closing_balances = defaultdict(lambda: {'credit': 0.0, 'debit': 0.0, 'balance': 0.0})
        for line in current_lines:
            if line.partner_id:
                pid = line.partner_id.id
                grouped_records[pid] += line
                closing_balances[pid]['credit'] += line.credit
                closing_balances[pid]['debit'] += line.debit
                closing_balances[pid]['balance'] += line.balance
              
        for pid in closing_balances:
            init = initial_balances.get(pid)
            if init:
                closing_balances[pid]['credit'] += init['credit']
                closing_balances[pid]['debit'] += init['debit']
                closing_balances[pid]['balance'] += init['balance']

        visible_partner_ids = set(grouped_records.keys())

        if not wizard.sh_start_date and not wizard.sh_end_date:
            all_domain = base_domain.copy()
            all_lines = self.env['account.move.line'].search(all_domain)
            visible_partner_ids = {line.partner_id.id for line in all_lines if line.partner_id}

        partners = self.env['res.partner'].browse(visible_partner_ids)

        return {
            'doc_ids': docids,
            'doc_model': 'sh.partner.ledger.wizard',
            'docs': wizard,
            'partners': partners,
            'grouped_records': grouped_records,
            'sh_start_date': wizard.sh_start_date,
            'sh_end_date': wizard.sh_end_date,
            'closing_balances': closing_balances,
            'initial_balances': initial_balances,
            'company': wizard.sh_company_id or self.env.company,
        }













# from collections import defaultdict
# from odoo import fields, models

# class ShPartnerLedgerWizard(models.TransientModel):
#     _name = 'sh.partner.ledger.wizard'
#     _description = "Partner Ledger Wizard"

#     sh_target_moves = fields.Selection([
#         ('posted', 'All Posted Entries'),
#         ('all', 'All Entries')
#     ], string="Target Moves", default='posted')

#     sh_initial_balance = fields.Boolean(string="Show Initial Balance")
#     sh_closing_balance = fields.Boolean(string="Show Closing Balance")
#     sh_reconsile_entry = fields.Boolean(string="Include Reconciled Entries")
#     sh_start_date = fields.Date(string="Start Date")
#     sh_end_date = fields.Date(string="End Date")
#     sh_payable_type = fields.Selection([
#         ('receivable', 'Receivable Accounts'),
#         ('receive_pay', 'Receivable and Payable Accounts')
#     ], string="Partner's")
#     sh_company_id = fields.Many2one('res.company', default=lambda self: self.env.company)
#     sh_partner_ids = fields.Many2many('res.partner', string="Partners")
#     sh_journals_ids = fields.Many2many('account.journal', string="Journals")

#     def partner_ledger_print(self):
#         return self.env.ref('sh_partner_ledger_balance.print_partner_ledger_report_action').report_action(self)


# class ReportPartnerLedger(models.AbstractModel):
#     _name = 'report.sh_partner_ledger_balance.print_partner_ledger_report'
#     _description = 'Partner Ledger Report'

#     def _get_report_values(self, docids, data=None):
#         wizard = self.env['sh.partner.ledger.wizard'].browse(docids)

#         base_domain = []
#         if wizard.sh_journals_ids:
#             base_domain.append(('journal_id', 'in', wizard.sh_journals_ids.ids))
#         if wizard.sh_partner_ids:
#             base_domain.append(('partner_id', 'in', wizard.sh_partner_ids.ids))

#         # 1. Get Initial Balances BEFORE start date
#         initial_domain = base_domain.copy()
#         if wizard.sh_start_date:
#             initial_domain.append(('date', '<', wizard.sh_start_date))
#         initial_lines = self.env['account.move.line'].search(initial_domain)

#         initial_balances = defaultdict(lambda: {'credit': 0.0, 'debit': 0.0, 'balance': 0.0})
#         for line in initial_lines:
#             if line.partner_id:
#                 pid = line.partner_id.id
#                 initial_balances[pid]['credit'] += line.credit
#                 initial_balances[pid]['debit'] += line.debit
#                 initial_balances[pid]['balance'] += line.balance

#         # 2. Get lines for selected date range
#         current_domain = base_domain.copy()
#         if wizard.sh_start_date:
#             current_domain.append(('date', '>=', wizard.sh_start_date))
#         if wizard.sh_end_date:
#             current_domain.append(('date', '<=', wizard.sh_end_date))
#         current_lines = self.env['account.move.line'].search(current_domain, order='partner_id, date')

#         grouped_records = defaultdict(lambda: self.env['account.move.line'])
#         closing_balances = defaultdict(lambda: {'credit': 0.0, 'debit': 0.0, 'balance': 0.0})
#         for line in current_lines:
#             if line.partner_id:
#                 pid = line.partner_id.id
#                 grouped_records[pid] += line
#                 closing_balances[pid]['credit'] += line.credit
#                 closing_balances[pid]['debit'] += line.debit
#                 closing_balances[pid]['balance'] += line.balance

#         partners = self.env['res.partner'].browse(grouped_records.keys() | initial_balances.keys())
        
#         return {
#             'doc_ids': docids,
#             'doc_model': 'sh.partner.ledger.wizard',
#             'docs': wizard,
#             'partners': partners,
#             'grouped_records': grouped_records,
#             'sh_start_date': wizard.sh_start_date,
#             'sh_end_date': wizard.sh_end_date,
#             'closing_balances': closing_balances,
#             'initial_balances': initial_balances,
#             'company': wizard.sh_company_id or self.env.company,
#         }



