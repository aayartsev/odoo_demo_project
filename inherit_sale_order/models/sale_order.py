from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    additional_field = fields.Char(
        string="Additional Field",
        help="Field for showing inheritance of model and adding additional field"
    )