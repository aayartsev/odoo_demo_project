import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)


class FirstModel(models.Model):
    _name = 'first.model'
    _description = 'Your first model'

    name = fields.Char(string='Name', help='Name of record')

    # field_one = fields.Integer(string='Field One', help='Value of Field One')

    field_two = fields.Float(
        string='Field Two',
        help='Value of Field Two',
    )

    field_three = fields.Integer(
        string='Field Three',
        help='Value of Field Three'
    )

    result_field = fields.Float(
        string='Result',
        help='Result of multiplying Field one and Field two',
        compute='_compute_result_field',
    )


    @api.depends('field_one', 'field_two')
    def _compute_result_field(self):
        for record in self:
            record.result_field = record.field_three * record.field_two

    def start_function(self):
        _logger.warning(_('You started function by button'))
