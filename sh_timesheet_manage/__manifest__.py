# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.


{
    'name': 'Timesheet Manage',
    'version': '1.0',
    'sequence': 10,
    'category': 'Timesheet/Timesheet',
    'summary': 'Manage whole Timesheet information in single module',
    'description': """
                    This module contains all the common features of Timesheet Management.
                """,
    'website': 'https://www.odoo.com/app/Timesheet',           
    'depends': ['base_setup','web','mail'],
    
    'data': [
        'Security/timesheet_security.xml',
        'Security/ir.model.access.csv',
        # 'Views/sh_timesheet_cron.xml',
        'Views/sh_tag_view.xml',
        'Views/sh_task_view.xml',
        'Views/sh_rejection_reason.xml',
        'Views/sh_timesheet_view.xml',
        'Views/sh_project_view.xml',
        'Views/sh_attendence_view.xml',
        'Views/sh_timesheet_emp_view.xml',
        'Views/timesheet_menus.xml'

    ],
    'application':True,
    'installable': True,
    'license': 'LGPL-3',
}
