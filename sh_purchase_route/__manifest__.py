# Copyright (C) Softhealer Technologies.
# Part of Softhealer Technologies.

{
    'name': 'Purchase Routes',
    'version': '1.0',
    'sequence': 10,
    'depends': ['base','web','purchase','stock',],
    'data': [
        'Views/sh_purchase_view.xml',
    ],
    'installable': True,
    'application': True,

    
    'license': 'LGPL-3',
}
