/** @odoo-module alias=theme_airproof.js_snippet_example */

import options from 'web_editor.snippets.options';

options.registry.AirproofTable = options.Class.extend({

    //--------------------------------------------------------------------------
    // Options
    //--------------------------------------------------------------------------

    /**
     * Имя функции должно соответствовать атрибуту пункта меню
     * например data-start-table-func вызовет функцию startTableFunc(переведет ее в camel case)
     *
     * @see this.selectClass for parameters
     */
    startTableFunc: function (previewMode, widgetValue, params) {
        // console.log("display")
        // console.log("previewMode", previewMode)
        // console.log("widgetValue", widgetValue)
        // console.log("params", params)
        const $table = this.$target.find('.table');
        let $descriptionElement = this.$target.find('.table-airproof-description')
        console.log("$descriptionElement", $descriptionElement)
        if ($descriptionElement.length === 0) {
            $descriptionElement = $(`<p class="table-airproof-description"> Awesome table description</p>`)
        }
        // const 

        // Classic
        // this.$target.find('.s_blockquote_avatar').toggleClass('d-none', widgetValue !== 'classic');

        // // Cover
        
        console.log("$table", $table)
        if(widgetValue == "top"){
            $descriptionElement.insertBefore($table)
        }
        if(widgetValue == "bottom"){
            $descriptionElement.insertAfter($table)
        }
        if(widgetValue == "without"){
            $descriptionElement.detach()
        }
        // if (widgetValue === 'cover') {
        //     $blockquote.css({"background-image": "url('/web/image/website.s_blockquote_cover_default_image')"});
        //     $blockquote.addClass('oe_img_bg o_bg_img_center');
        //     if (!$blockquote.find('.o_we_bg_filter').length) {
        //         const bgFilterEl = document.createElement('div');
        //         bgFilterEl.classList.add('o_we_bg_filter', 'bg-white-50');
        //         $blockquote.prepend(bgFilterEl);
        //     }
        // } else {
        //     $blockquote.css({"background-image": ""});
        //     $blockquote.css({"background-position": ""});
        //     $blockquote.removeClass('oe_img_bg o_bg_img_center');
        //     $blockquote.find('.o_we_bg_filter').remove();
        //     $blockquote.find('.s_blockquote_filter').contents().unwrap(); // Compatibility
        // }

        // // Minimalist
        // this.$target.find('.s_blockquote_icon').toggleClass('d-none', widgetValue === 'minimalist');
        // this.$target.find('footer').toggleClass('d-none', widgetValue === 'minimalist');
    },
});

