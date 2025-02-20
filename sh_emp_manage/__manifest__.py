# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Employee manage',
    'version': '1.0',
    'summary': 'manage the employee management system',
    'sequence': 10,
    'description': """
Invoicing & Payments
====================
The specific and easy-to-use Invoicing system in Odoo allows you to keep track of your accounting, even when you are not an accountant. It provides an easy way to follow up on your vendors and customers.

You could use this simplified accounting in case you work with an (external) account to keep your books, and you still want to keep track of payments. This module also offers you an easy method of registering payments, without having to encode complete abstracts of account.
    """,
    'category': 'Employee/Employee',
    'website': 'https://www.odoo.com/app/employee',
    'depends': ['base_setup', 'web','sh_library_manage','sale'],
    'icon':'/sh_emp_manage/static/description/icon.png',
    
    'data':[
        'security/ir.model.access.csv',
        'views/sh_emp_view.xml',
        'views/sh_job_view.xml',
        'views/sh_department_view.xml',
        # 'views/sh_calendar_view.xml',
        'views/sh_emp_cat_view.xml',
        'views/sh_emp_menu.xml',
        'views/sh_compute_view.xml',
        'views/sh_onchange_view.xml',
        'views/sh_trip_view.xml',
        'views/sh_action_view.xml',
        'views/sh_task_view.xml',
        'views/sh_test_view.xml',
        'views/sh_hospital_menu.xml',
        'views/sh_doctor_view.xml',
        'views/sh_patient_view.xml',
        'views/sh_diagnosis_view.xml',
        'views/sh_age_category_view.xml',
        'views/sh_res_partner_view.xml',
        'views/sh_product_view.xml',
        'views/sh_account_tax_view.xml',
        'views/sh_sale_order_view.xml',
        # 'views/sh_sale_order_line_view.xml',
        'views/sh_sale_menu.xml',
        'views/sh_orm_create_view.xml',
        'views/sh_orm_employee_view.xml',
        'views/sh_orm_category_view.xml',
        'views/sh_orm_menu.xml',
        'views/sh_inheritance.xml',
        'views/sh_note.xml',

        
        
        
        
    ],
    
     'assets': {
        'web.assets_backend': [
            'sh_emp_manage/static/src/css/sh_emp.css',
            # 'sh_real_estate_management/static/src/css/custom_menu.css',
        ],
        

},
    
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
