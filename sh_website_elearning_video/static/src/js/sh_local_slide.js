// /** @odoo-module **/

// // import publicWidget from 'web.public.widget';
// import { Fullscreen } from '@website_slides/js/slides_course_fullscreen_player';
// import { videoTemplates } from '@website_slides/js/slides_course_fullscreen_player';

// // 🟢 Extend the default videoTemplates registry to include local video logic (optional if fallback needed)
// videoTemplates.local_video = (slide) => {
//     return `
//         <div class="player ratio ratio-16x9 embed-responsive-item h-100">
//             <video controls autoplay class="w-100 h-100" style="max-height: 90vh;">
//                 <source src="/web/content/slide.slide/${slide.id}/sh_attachment?filename_field=sh_attachment_name" type="video/mp4" />
//                 Your browser does not support the video tag.
//             </video>
//         </div>
//     `;
// };

// // 🟢 Patch the Fullscreen class
// Fullscreen.include({
//     async _renderSlide() {
//         const slide = this._slideValue;
//         const $content = this.$('.o_wslides_fs_content');
//         $content.empty();

//         // ✅ Custom condition for binary video
//         if (slide.category === 'video' && slide.sh_document_type === 'file' && slide.sh_attachment) {
//             const html = `
//                 <div class="player ratio ratio-16x9 embed-responsive-item h-100">
//                     <video controls autoplay class="w-100 h-100" style="max-height: 90vh;">
//                         <source src="/web/content/slide.slide/${slide.id}/sh_attachment?filename_field=sh_attachment_name" type="video/mp4" />
//                         Your browser does not support the video tag.
//                     </video>
//                 </div>
//             `;
//             $content.html(html);
//         }
//         // ✅ Fallback to existing templates (YouTube, Vimeo, etc.)
//         else if (slide.category === 'video') {
//             const videoSource = slide.video_source_type || 'youtube';
//             const render = videoTemplates[videoSource];
//             if (render) {
//                 $content.html(render(slide));
//             }
//         }
//         // ✅ Document type (PDF, etc.)
//         else if (slide.category === 'document') {
//             $content.html(`
//                 <div class="ratio h-100">
//                     <iframe src="${slide.embedUrl}" class="o_wslides_iframe_viewer" allowfullscreen frameborder="0"></iframe>
//                 </div>
//             `);
//         }
//         // ✅ Infographic type
//         else if (slide.category === 'infographic') {
//             $content.html(`
//                 <div class="o_wslides_fs_player w-100 h-100 overflow-auto d-flex align-items-start justify-content-center">
//                     <img src="/web/image/slide.slide/${slide.id}/image_1024" class="img-fluid position-relative m-auto" alt="Slide image"/>
//                 </div>
//             `);
//         }
//     }
// });






    // odoo.define('sh_website_elearning_video.sh_local_slide', function (require) {
    //     'use strict';

    //     const SlideFullscreenPlayer = require('@website_slides/js/slides_course_fullscreen_player');
    //     // const publicWidget = require('web.public.widget');

    //     SlideFullscreenPlayer.include({
    //         _renderVideo: function () {
    //             const slide = this._slideValue;

    //             // Your custom condition: Check if it's a 'video' category and local file
    //             if (slide.category === 'video' && slide.sh_document_type === 'file' && slide.sh_attachment) {
    //                 // Render your local video player
    //                 this.$player.html(`
    //                     <div class="player ratio ratio-16x9 embed-responsive-item h-100">
    //                         <video controls autoplay class="w-100 h-100" style="max-height: 90vh;">
    //                             <source src="/web/content/slide.slide/${slide.id}/sh_attachment?filename_field=sh_attachment_name" type="video/mp4"/>
    //                             Your browser does not support the video tag.
    //                         </video>
    //                     </div>
    //                 `);
    //             } else {
    //                 // fallback to default behavior
    //                 this._super.apply(this, arguments);
    //             }
    //         },
    //     });
    // });



odoo.define('sh_website_elearning_video.sh_local_slide', [
    '@website_slides/js/slides_course_fullscreen_player',
], function (SlideFullscreenPlayer) {
    'use strict';

    SlideFullscreenPlayer.include({
        _renderVideo: function () {
            const slide = this._slideValue;

            // Your custom logic for local video
            if (slide.category === 'video' && slide.sh_document_type === 'file' && slide.sh_attachment) {
                this.$player.html(`
                    <div class="player ratio ratio-16x9 embed-responsive-item h-100">
                        <video controls autoplay class="w-100 h-100" style="max-height: 90vh;">
                            <source src="/web/content/slide.slide/${slide.id}/sh_attachment?filename_field=sh_attachment_name" type="video/mp4"/>
                            Your browser does not support the video tag.
                        </video>
                    </div>
                `);
            } else {
                // fallback to default behavior
                this._super.apply(this, arguments);
            }
        },
    });
});

