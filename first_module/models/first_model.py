import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)


class FirstModel(models.Model):
    _name = 'first.model'
    _description = 'Your first model'

    name = fields.Char(string='Name', help='Name of record')

    field_one = fields.Integer(string='Field One', help='Value of Field One')

    field_two = fields.Float(
        string='Field Two',
        help='Value of Field Two',
    )

    result_field = fields.Float(
        string='Result',
        help='Result of multiplying Field one and Field two',
        compute='_compute_result_field',
    )

    @api.depends('field_one', 'field_two')
    def _compute_result_field(self):
        for record in self:
            record.result_field = record.field_one * record.field_two

    def start_function(self):
        _logger.warning(_('You started function by button'))

class ParticularReport(models.AbstractModel):
    _name = "report.first_module.print_form_001_template"
    _description = "Extend of print form"

    @api.model
    def _get_report_values(self, docids, data=None):
        """
        Функция для расширения данных подаваемых на печать в шаблон
        param : docids : list : список id записей модели, к которой прикреплен шаблон для печати
        param : data : {} : дополнительные которые содержат в себе метаинформацию
        return : dict : словарь данными, используемыми в шаблоне
        """
        first_model_recordset = self.env["first.model"].browse(docids)
        ...
        return {
            "doc_ids": docids,
            "docs": first_model_recordset,
            "data": data,
        }