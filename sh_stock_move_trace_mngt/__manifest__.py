# Copyright (C) Softhealer Technologies.
# Part of Softhealer Technologies.
{
    'name': 'Stock Move Traceability from Sales/purchase order receipt',
    'version': '1.0',
    'sequence': 10,
    'author' : 'Softhealer Technologies',
    'depends': ['base','web','sale','purchase','stock'],
    'data': [
        'Views/sh_stock_move.xml'
    ],
    'installable': True,
    'application': True,

    
    'license': 'LGPL-3',
}
