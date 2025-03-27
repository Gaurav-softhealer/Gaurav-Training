# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.


{
    'name': 'Sale Order Automatic Workflow',
    'version': '1.0',
    'sequence': 10,
    'category': 'sale/sale',
    'summary': 'Manage whole sale order automatic workflow',
    'description': """
                    This module contains sale order automatic workflow.
                """,
    'website': 'https://www.odoo.com/app/saleOrderAutomatic',           
    'depends': ['base_setup','web','mail','sale'],
    
    'data': [
        'Security/ir.model.access.csv',
        'Views/sh_sale_auto_workflow_view.xml',
        'Views/sh_sale_config_view.xml',
        'Views/sale_order_inherit_view.xml',

    ],
    'application':True,
    'installable': True,
    'license': 'LGPL-3',
}
