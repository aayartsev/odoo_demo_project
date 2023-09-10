odoo.define('website_first_module.publishRecordButton', function (require) {
    "use strict";

    var publicWidget = require('web.public.widget');
    var rpc = require('web.rpc');

    publicWidget.registry.publishRecordButton = publicWidget.Widget.extend({
        selector: '.toggle-published',
        events: {
            'click': '_onClickPublishButton',
        },

        _onClickPublishButton(ev) {
            ev.preventDefault();
            ev.stopPropagation();
            const modelName = $(ev.currentTarget).data('model'); 
            const resId = $(ev.currentTarget).data('res-id');
            const isPublished = $(ev.currentTarget).data('is-published');
            rpc.query({
                args: [resId, {
                    "is_published": !isPublished
                }],
                model: modelName,
                method: 'write',
            })
            .then(response => {
                const iconElement = $(ev.currentTarget).find("i")
                if(response){
                    $(ev.currentTarget).data('is-published', !isPublished)
                    if(isPublished){
                        iconElement.addClass('fa-eye-slash text-danger').removeClass('fa-eye text-success');
                    }else{
                        iconElement.addClass('fa-eye text-success').removeClass('fa-eye-slash text-danger');
                    }
                }
            });
        },
    });

    return publicWidget.registry.modalWithDocView;
})