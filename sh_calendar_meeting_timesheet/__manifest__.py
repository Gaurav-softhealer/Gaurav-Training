# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.


{
    'name': 'Calendar Meeting Timesheet',
    'version': '1.0',
    'sequence': 10,
    'category': 'meeting',
    'summary': 'Manage the calendar meeting timesheet',
    'description': """
                    This module contains all the information about the calendar meeting timesheet.
                """,
    'website': 'https://www.odoo.com/app/meeting',           
    'depends': ['base_setup','web','sale_management','product','calendar','project','hr_timesheet'],
    
    'data': [
        # 'Security/ir.model.access.csv',
        'Views/calendar_meeting_inherit_view.xml',

        
    ],
    
    
    'application':True,
    'installable': True,
    'license': 'LGPL-3',
}
