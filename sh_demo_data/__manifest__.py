# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.


{
    'name': 'demo data Manage',
    'version': '1.0',
    'sequence': 10,
    'category': 'demo/demo',
    'summary': 'Manage whole demo data information in single module',
    'description': """
                    This module contains all the common features of demo data Management.
                """,
    'website': 'https://www.odoo.com/app/demo',           
    'depends': ['base_setup','web',],
    
    # 'icon':'/sh_emp_manage/static/description/icon.png',
    'demo':[
        'demo/demo_data.xml'
        ],
    
    'data': [
        'Security/ir.model.access.csv',
        'Views/demo_profile_view.xml',
        
    ],
    'application':True,
    'installable': True,
    'license': 'LGPL-3',
}
