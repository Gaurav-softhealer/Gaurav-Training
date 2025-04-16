# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.


{
    'name': 'Manufacturing Custom',
    'version': '1.0',
    'sequence': 10,
    'category': 'manufacturing',
    'summary': 'Manage whole manufacturing checklist',
    'description': """
                    This module contains Manage whole manufacturing checklist.
                """,
    'website': 'https://www.odoo.com/app/manufacturing',           
    'depends': ['base_setup','web','sale_management','product','mrp'],
    
    'data': [
        'Security/sh_checklist_security.xml',
        'Security/ir.model.access.csv',
        'Views/sh_manufacturing_view.xml',
        'Views/sh_manufacturing_template.xml',
        'Views/sh_import_checklist.xml',
        'Views/sh_manufacturing_order.xml',
        'Views/sh_checklist_line.xml',
    ],
    
    
    'application':True,
    'installable': True,
    'license': 'LGPL-3',
}
