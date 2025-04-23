# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.


{
    'name': 'Pharmacy Management System',
    'version': '1.0',
    'sequence': 10,
    'category': 'management',
    'summary': 'Manage the bussiness of the pharmacy',
    'description': """
                    This module is used to manage bussiness of the  pharmacy.
                """,
    'website': 'https://www.odoo.com/app/pharmacy',           
    'depends': ['base_setup','web','sale','contacts','sale_management','stock'],
    
    'icon':'/sh_pharmacy_mngt/static/description/pharmacy.png',
    
    'data': [
        'Security/ir.model.access.csv',
        'Views/sh_allergy_type_view.xml',
        'Views/sh_allergy_view.xml',
        'Views/sh_medicine_form_view.xml',
        'Views/sh_medicine_ingredient_view.xml',
        'Views/sh_commission_type_view.xml',
        'Views/sh_specialization_category.xml',
        'Views/sh_pharmacy_doctor_view.xml',
        'Views/sh_pharmacy_patient_view.xml',
        'Views/sh_pharmacy_product_view.xml',
        'Views/sh_pharmacy_sale_order_view.xml',
        'Views/sh_pharmacy_vendor_view.xml',
        'Views/sh_pharmacy_menu.xml',


        
    ],
    'application':True,
    'installable': True,
    'license': 'LGPL-3',
}
