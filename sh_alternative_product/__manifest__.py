# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.


{
    'name': 'Alternative Product',
    'version': '1.0',
    'sequence': 10,
    'category': 'alternative',
    'summary': 'Manage whole alternative product',
    'description': """
                    This module contains all the common features alternative product.
                """,
    'website': 'https://www.odoo.com/app/alternative',           
    'depends': ['base_setup','web','sale_management','product'],
    
    'data': [
        
        'Security/sh_alternative_product_security.xml',
        'Security/ir.model.access.csv',
        'Views/sh_product_variant_view.xml',
        'Views/sh_product_varient_wizard.xml',

        
    ],
    
    
    'application':True,
    'installable': True,
    'license': 'LGPL-3',
}
