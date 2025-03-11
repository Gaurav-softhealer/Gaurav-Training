# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.


{
    'name': 'Music Academy',
    'version': '1.0',
    'sequence': 10,
    'category': 'Music/Music Academy',
    'summary': 'manage information about the music academy',
    'description': """
                    This whole module is used to manage information about the music academy.
                """,
    'website': 'https://www.odoo.com/app/MusicAcademy',           
    'depends': ['base_setup','web','mail'],
    
    'data': [
        'Security/ir.model.access.csv',
        'Views/music_student_view.xml',
        'Views/music_equipment_view.xml',
        'Views/music_lesson_view.xml',
        'Views/music_teacher_view.xml',
        'Views/music_service_view.xml',
        'Views/music_instrument_view.xml',
        'Views/music_classes_view.xml',
        'Views/music_academy_menus.xml',
    ],
    'application':True,
    'installable': True,
    'license': 'LGPL-3',
}
