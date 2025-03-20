# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.


{
    'name': 'Support Ticket',
    'version': '1.0',
    'sequence': 10,
    'category': 'Ticket/Ticket',
    'summary': 'Manage whole Support Tickett information in single module',
    'description': """
                    This module contains all the common features of support Ticket Management.
                """,
    'website': 'https://www.odoo.com/app/Ticket',           
    'depends': ['base_setup','web','mail','account','contacts'],
    
    'demo':[
        'demo/demo_data.xml',
    ],
    
    'data': [
        'Security/support_ticket_security.xml',
        'Security/ir.model.access.csv',
    
        'Views/ticket_action_server.xml',
        'Views/ticket_done_reason.xml',
        'Views/customer_support_view.xml',
        'Views/support_ticket_view.xml',
        'Views/ticket_squence.xml',
        'Views/ticket_cron_view.xml',

    ],
    'application':True,
    'installable': True,
    'license': 'LGPL-3',
}
