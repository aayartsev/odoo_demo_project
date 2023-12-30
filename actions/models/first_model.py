import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)


class FirstModel(models.Model):
    _inherit = 'first.model'

    to_print = fields.Boolean(
        string="To print",
        help="If this param will be enabled, it will be added to report"
    )

    @api.model
    def call_action(self):
        report_action = self.env.ref("actions.report_action_example").read()[0]
        docs = self.search(
            [('to_print', '=', True)])
        if docs:
            report_action.update({
                "context": {
                    "active_ids": docs.ids
                }
            })
            return report_action
        else:
            return {
                'type': 'ir.actions.client',
                'tag': 'actions.client_action_example',
                'name': 'Nothing to print',
                'params': {
                    'message': _('Nothing to print')
                },
            }