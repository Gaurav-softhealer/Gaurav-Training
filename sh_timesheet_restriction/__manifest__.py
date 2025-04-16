# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.


{
    'name': 'Timesheet Restriction',
    'version': '1.0',
    'sequence': 10,
    'category': 'Timesheet/Timesheet',
    'summary': 'Manage timesheet restriction',
    'description': """
                    This module timesheet restriction of Timesheet Management.
                """,
    'website': 'https://www.odoo.com/app/Timesheet_restriction',           
    'depends': ['base_setup','web','mail','hr_timesheet','project'],
    
    'data': [
            'Security/timesheet_restriction_security.xml',
            'Views/sh_timesheet_restricted_config_view.xml',
    ],
    'application':True,
    'installable': True,
    'license': 'LGPL-3',
}
