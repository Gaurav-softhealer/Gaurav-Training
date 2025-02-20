# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.


{
    'name': 'Sale Manage',
    'version': '1.0',
    'sequence': 10,
    'category': 'sh_sale/sh_sale',
    'summary': 'Manage whole sale information in single module',
    'description': """
                    This module contains all the common features of sale Management.
                """,
    'website': 'https://www.odoo.com/app/sh_sale',           
    'depends': ['base_setup','web',],
    
    'data': [
        'Security/ir.model.access.csv',
        'Views/sh_res_partner_view.xml',
        'Views/sh_product_view.xml',
        'Views/sh_account_tax_view.xml',
        'Views/sh_sale_order_view.xml',
        'Views/sh_sale_menu.xml',

        
    ],
    'application':True,
    'installable': True,
    'license': 'LGPL-3',
}
