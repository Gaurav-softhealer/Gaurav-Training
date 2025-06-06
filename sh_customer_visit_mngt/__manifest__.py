# Copyright (C) Softhealer Technologies.
# Part of Softhealer Technologies.
{
    'name': 'Customer Visit Management',
    'version': '1.0',
    'sequence': 10,
    'depends': ['base','web','crm','contacts'],
    'data': [
        'Security/ir.model.access.csv',
        'Views/sh_sales_visit_view.xml',
        'Views/sh_sequence_view.xml',
        'Views/sh_sale_vist_cron.xml',
        'Views/sh_res_partner_view.xml',
        'Views/sh_cancel_reason_view.xml',
        'Wizard/sh_cancel_reason_wizard.xml',
    ],
    'installable': True,
    'application': True,

    
    'license': 'LGPL-3',
}
