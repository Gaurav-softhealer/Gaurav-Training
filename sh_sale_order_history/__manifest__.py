# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.


{
    'name': 'Sale Order History',
    'version': '1.0',
    'sequence': 10,
    'category': 'Sale Order/Sale Order',
    'summary': 'Manage whole sale order history',
    'description': """
                    This module contains Manage whole sale order history.
                """,
    'website': 'https://www.odoo.com/app/saleOrderHistory',           
    'depends': ['base_setup','web','mail','account','contacts','sale'],

    
    'data': [
        'Security/sale_order_history_security.xml',
        'Security/ir.model.access.csv',
        'Views/sale_order_stage_view.xml',
        'Views/sh_sale_order_history_view.xml',
        'Views/sale_order_history_config_view.xml',
        'Views/sh_template.xml',

    ],
    'application':True,
    'installable': True,
    'license': 'LGPL-3',
}
