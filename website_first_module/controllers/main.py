from odoo import http
from odoo.http import request
from odoo.osv import expression

import werkzeug



class WebsiteFirstModelDataController(http.Controller):

    @http.route(["/records"], type="http", auth="public",  website=True, sitemap=True)
    def get_records_list(self):
        domain = []
        if not request.env.user.has_group("base.group_user"):
            domain = expression.AND([domain, [("is_published", "=", True)]])
        all_records = request.env["first.model"].search(domain)
        values = {
            
            "all_records": all_records,
        }
        # наличие в декораторе параметра website=True автоматически добавит при рендеринге шаблона 
        # добавит рекордсет из одной записи модели "website", который определен в модуле website
        # sitemap=True ????
        return request.render("website_first_module.first_model_public_list", values)

    @http.route(["""/records/<model("first.model"):first_model_record_id>"""], type="http", auth="public", website=True, sitemap=True)
    def get_records_item(self, first_model_record_id):
        all_records = request.env["first.model"].search([("is_published", "=", True)])

        if first_model_record_id not in all_records and not request.env.user.has_group("base.group_user"):
            raise request.not_found()
        values = {
            "main_object": first_model_record_id,
        }
        return request.render("website_first_module.first_model_public_item", values)