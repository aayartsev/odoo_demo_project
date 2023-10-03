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
        const $table = this.$target.find('.table');
        let $descriptionElement = this.$target.find('.table-airproof-description')

        if ($descriptionElement.length === 0) {
            $descriptionElement = $(`<p class="table-airproof-description"> Awesome table description</p>`)
        }
        
        if(widgetValue == "top"){
            $descriptionElement.show()
            $descriptionElement.insertBefore($table)
        }
        if(widgetValue == "bottom"){
            $descriptionElement.show()
            $descriptionElement.insertAfter($table)
        }
        if(widgetValue == "without"){
            if(previewMode){
                $descriptionElement.hide()
            }else{
                $descriptionElement.detach()
            }
        }
    },
});

