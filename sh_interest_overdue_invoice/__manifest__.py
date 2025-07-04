# Copyright (C) Softhealer Technologies.
# Part of Softhealer Technologies.

{
    'name': 'Interest on Overdue Invoice',
    'version': '1.0',
    'sequence': 10,
    'depends': ['base','web','sale','account'],
    'author':'Softhealer Technologies',
    'data': [

        'Views/sh_res_user_group.xml',
        'Views/sh_account_move.xml',
        'Views/ir_cron_data.xml',
        'Views/sh_account_payment_term.xml',
    ],
    
    'installable': True,
    'application': True,

    
    'license': 'LGPL-3',
}