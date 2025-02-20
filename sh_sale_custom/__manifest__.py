# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.


{
    'name': 'Sale Custom',
    'version': '1.0',
    'sequence': 10,
    'category': 'sale custom',
    'summary': 'Manage the custom module',
    'description': """
                    This module is used to manage cutom sale module.
                """,
    'website': 'https://www.odoo.com/app/custom_sale',           
    'depends': ['base_setup','web','sale'],
    
    'data': [
        'Security/ir.model.access.csv',
        'Views/sh_note_view.xml',
        'Views/sh_sale_view.xml',
        'Views/sh_sale_order_line_view.xml',


        
    ],
    'application':True,
    'installable': True,
    'license': 'LGPL-3',
}
