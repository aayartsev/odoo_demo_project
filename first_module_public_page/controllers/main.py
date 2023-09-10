from odoo import http
from odoo.http import request



class FirstModelDataController(http.Controller):

    @http.route(["/records/"], type="http", auth="public")
    def get_records_list(self):
        all_records = request.env["first.model"].search([])
        values = {
            "all_records": all_records,
        }
        return request.render("first_module_public_page.first_model_public_list", values)

    @http.route(["""/records/<model("first.model"):first_model_record_id>"""], type="http", auth="user")
    def get_records_item(self, first_model_record_id):
        values = {
            "record": first_model_record_id,
        }
        return request.render("first_module_public_page.first_model_public_item", values)