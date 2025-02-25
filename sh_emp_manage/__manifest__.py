# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.


{
    'name': 'Employee Manage',
    'version': '1.0',
    'sequence': 10,
    'category': 'employee/employee',
    'summary': 'Manage whole employee information in single amodule',
    'description': """
                    This module contains all the common features of employee Management.
                """,
    'website': 'https://www.odoo.com/app/employee',           
    'depends': ['base_setup','web',],
    
    'icon':'/sh_emp_manage/static/description/icon.png',
    
    'data': [
        'Security/ir.model.access.csv',
        'Views/sh_emp_view.xml',
        'Views/sh_job_view.xml',
        'Views/sh_department_view.xml',
        'Views/sh_emp_cat_view.xml',
        'Views/sh_emp_menu.xml',    
    ],
    'application':True,
    'installable': True,
    'license': 'LGPL-3',
}
