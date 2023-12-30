/** @odoo-module **/
import { registry } from "@web/core/registry";

function ClientActionExample(env, action){

    const message = action.params.message
        var notification = {
            type: 'info',
            sticky: true,
        };
        env.services.notification.add(message, notification)

        const url_action = {
            type: "ir.actions.act_url", 
            url: "https://blog.yartsev.by/odoo_tutorials/004_developers_tutorial/006_actions/001_actions.html",
            target: "new"
        }
        env.services.action.doAction(
            url_action,
        );
}
registry.category("actions").add("actions.client_action_example", ClientActionExample);

// This is example for 14.0 and older versions

// odoo.define('actions.js_action', function (require){
//     var core = require('web.core')
//     var _t = core._t;
//     function nothingToPrintAction(env, action){
//         env.do_notify(false, _t("Nothing to print"))
//     }
//     core.action_registry.add("actions.nothing_to_print", nothingToPrintAction);
// })