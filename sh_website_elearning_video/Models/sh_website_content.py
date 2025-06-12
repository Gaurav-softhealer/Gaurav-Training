from odoo import fields,models,api,http,_
from mimetypes import guess_type
from odoo.http import request
from markupsafe import Markup
from werkzeug import urls


class ShWebsiteContent(models.Model):
    _inherit="slide.slide"
    
    sh_document_type=fields.Selection([
        ('url','URL'),
        ('file','File')
    ],string="Document Type")
    
    sh_attachment=fields.Binary(string="Attachment",attachment=True,filename="sh_attachment_name")
    sh_attachment_name = fields.Char(string="Filename",store=True)
    test=fields.Char()
    
    # @api.depends('slide_type')
    # def _compute_slide_icon_class(self):
    #     super()._compute_slide_icon_class()

    #     # Add or override additional custom types
    #     custom_icons = {
    #         'local_video': 'fa-youtube-play',
    #     }

    #     for slide in self:
    #         # If custom type, override
    #         if slide.slide_type in custom_icons:
    #             slide.slide_icon_class = custom_icons[slide.slide_type]

    @api.depends('slide_category', 'google_drive_id', 'video_source_type', 'youtube_id')
    def _compute_embed_code(self):
        super()._compute_embed_code() 

        for slide in self:
            print(f"\n\n\n\t--------------> 39 ",slide.video_source_type)
            if slide.video_source_type==False and slide.slide_category == 'video' and slide.sh_document_type == 'file' and slide.sh_attachment:
                slide.embed_code = Markup(f"""
                    <video controls autoplay style="width: 100%; max-height: 90vh;">
                        <source src="/web/content/slide.slide/{slide.id}/sh_attachment?filename_field=sh_attachment_name" type="video/mp4"/>
                        Your browser does not support the video tag.
                    </video>
                """)
  
class SlideVideoController(http.Controller):  
    @http.route(['/slides/slide/video'], type='http', auth='user')
    def video_display(self,**kwargs):
        print(f"\n\n\n\t--------------> 20 hello")
        slide = request.env['slide.slide'].sudo().search([('sh_attachment', '!=', False)], limit=1)
        # return request.render('sh_website_elearning_video.local_video')
        return request.render('sh_website_elearning_video.local_video',{'slide':slide})



    
    
