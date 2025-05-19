# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.


{
    'name': 'Custom Web Form',
    'version': '1.0',
    'sequence': 10,
    'category': 'All',
    'summary': 'This module is used custom web form',
    'description': """
                    This module is used custom web form.
                """,
    'website': 'https://www.odoo.com/app/custom_web_form',           
    'depends': ['base_setup','web','portal','website'],
    
    'data': [
        'Security/ir.model.access.csv',
        'Views/sh_custom_web_form_user.xml',
        'Views/sh_custom_form_controller_view.xml',
        'Views/sh_user_update_form.xml',
        'Views/web_form_login_template.xml',
        'Views/web_form_signup_template.xml',


    ],
  
    'application':True,
    'installable': True,
    'license': 'LGPL-3',
}
