import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)


class FirstModel(models.Model):
    _inherit = 'first.model'

    one_partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Partner Domain 1",
        help="Partner selection for domain example 1",
        domain=[("name", "!=", "Deco Addict")],
    )

    two_partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Partner Domain 2",
        help="Partner selection for domain example 2",
        domain="[('name', '!=', 'Deco Addict')]",
    )

    three_partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Partner Domain 3",
        help="Partner selection for domain example 3",
        domain=lambda self: self.get_partner_domain(),
    )

    four_partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Partner Domain 4",
        help="Partner selection for domain example 4(see form view)",
    )

    five_partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Partner Domain 5",
        help="Partner selection for domain example 5(see form view)",
    )

    six_partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Partner Domain 6",
        help="Partner selection for domain example 6(res_partner.py)",
    )


    def get_partner_domain(self):
        domain = [("name", "!=", "Deco Addict")]
        return domain
    
    def set_one_partner_id(self):
        self.one_partner_id = self.env["res.partner"].search(
            [
                ("name", "=", "Deco Addict")
            ]
        )