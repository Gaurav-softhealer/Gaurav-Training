# Copyright (C) Softhealer Technologies.
# Part of Softhealer Technologies.

{
    'name': 'Multi Website Country',
    'version': '1.0',
    'sequence': 10,
    'depends': ['base','web','website','product','sale','website_sale'],
    'author':'Softhealer Technologies',
    'data': [

        'Views/sh_country_group.xml',
        'Views/sh_country_wizard.xml',
        'Views/sh_country_group_menu.xml',
        'Views/sh_setting_configuration.xml',
    ],
    
    'installable': True,
    'application': True,

    
    'license': 'LGPL-3',
}