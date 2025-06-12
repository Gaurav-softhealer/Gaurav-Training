# Copyright (C) Softhealer Technologies.
# Part of Softhealer Technologies.
{
    'name': 'eLearning Video Uploader',
    'version': '1.0',
    'sequence': 10,
    'depends': ['base','web','website','website_slides'],
    'author' : 'Softhealer Technologies',
    'data': [
        'Views/sh_website_content_view.xml',
        # 'Views/sh_website_slides_template.xml',
        # 'Views/sh_assets.xml',
        
    ],
    
    'assets': {
        'web.assets_frontend': [
            'sh_website_elearning_video/static/src/js/sh_local_slide.js',
        ],
        'website_slides.assets_frontend': [
            'sh_website_elearning_video/static/src/js/sh_local_slide.js',
        ],
    },


        
    'installable': True,
    'application': True,

    
    'license': 'LGPL-3',
}
