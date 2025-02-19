# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Library Management',
    'version': '1.0',
    'summary': 'manage the Library management system',
    'sequence': 10,
    'description': """
Invoicing & Payments
====================
The specific and easy-to-use Invoicing system in Odoo allows you to keep track of your accounting, even when you are not an accountant. It provides an easy way to follow up on your vendors and customers.

You could use this simplified accounting in case you work with an (external) account to keep your books, and you still want to keep track of payments. This module also offers you an easy method of registering payments, without having to encode complete abstracts of account.
    """,
    'category': 'Library/Library',
    'website': 'https://www.odoo.com/app/library',
    'depends': ['base_setup', 'web'],
    
    'icon':'/sh_library_manage/static/description/library.png',
    
    'data':[
        'security/ir.model.access.csv',
        'Views/sh_library_book_view.xml',
        'Views/sh_library_category_view.xml',
        'Views/sh_library_member_view.xml',
        'Views/sh_library_borrow_view.xml',
        'Views/my_sequence.xml',
    ],
    
     
    
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
