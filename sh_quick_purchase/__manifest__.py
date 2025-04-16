# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.


{
    'name': 'Quick Purchase Product',
    'version': '1.0',
    'sequence': 10,
    'category': 'purchase',
    'summary': 'Manage the quick purchase product',
    'description': """
                    This module is used to manage quick purchase product.
                """,
    'website': 'https://www.odoo.com/app/custom_sale',           
    'depends': ['base_setup','web','sale','crm','contacts','sale_management','stock','purchase'],
    
    'data': [
        'Security/sh_quick_purchase_security.xml',
        'Security/ir.model.access.csv',
        'Views/sh_quick_purchase_view.xml',
        'Views/sh_quick_purchase_line_view.xml',



        
    ],
    'application':True,
    'installable': True,
    'license': 'LGPL-3',
}
