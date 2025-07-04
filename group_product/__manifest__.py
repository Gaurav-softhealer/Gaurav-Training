# -*- coding: utf-8 -*-
{
    'name': "Merge Products To Variant",

    'summary': """
       Merge Products To Variant""",

    'description': """
       Merge Products To Variant
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale','product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/attribute_views.xml', 
        'views/views.xml',
    ],
}
