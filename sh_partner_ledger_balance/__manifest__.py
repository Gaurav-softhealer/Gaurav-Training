# Copyright (C) Softhealer Technologies.
# Part of Softhealer Technologies.

{
    'name': 'Partner Ledger Balance',
    'version': '1.0',
    'sequence': 10,
    'depends': ['base','web','account'],
    'author':'Softhealer Technologies',
    'data': [
        'Security/ir.model.access.csv',
        'Reports/sh_partner_ledger_report.xml',
        'Views/sh_partner_ledger_wizard.xml',
        'Views/sh_partner_ledger_menu.xml',
    ],
    'installable': True,
    'application': True,

    
    'license': 'LGPL-3',
}
