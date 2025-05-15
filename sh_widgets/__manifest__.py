# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.


{
    'name': 'Custom Widgets',
    'version': '1.0',
    'sequence': 10,
    'category': 'All',
    'summary': 'This module is used for manage custom wizards',
    'description': """
                    This module is used for manage custom wizards.
                """,
    'website': 'https://www.odoo.com/app/custom_widget',           
    'depends': ['base_setup','web','product','sale'],
    
    'data': [
        'Views/product_product.xml'

    ],
    
    'assets':{
        'web.assets_backend':[
            'sh_widgets/static/src/js/custom_slider_widget.js',
            'sh_widgets/static/src/xml/custom_slider_widget.xml',
        ]
    },
    
    'application':True,
    'installable': True,
    'license': 'LGPL-3',
}
