# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.


{
    'name': 'School Manage',
    'version': '1.0',
    'sequence': 10,
    'category': 'School/School',
    'summary': 'Manage whole school information in single amodule',
    'description': """
                    This module contains all the common features of school Management.
                """,
    'website': 'https://www.odoo.com/app/school',           
    'depends': ['base_setup','web',],
    
    'data': [
        'security/ir.model.access.csv',
        'views/sh_student_view.xml',
        'views/sh_school_department_view.xml',
        'views/sh_school_faculty_view.xml',
        'views/sh_school_subject_view.xml',
        'views/sh_school_semester_view.xml',
        'views/sh_menus.xml',
        'views/my_sequence.xml'
        
    ],
    'application':True,
    'installable': True,
    'license': 'LGPL-3',
}
