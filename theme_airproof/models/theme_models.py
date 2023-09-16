from odoo import models


class ThemeAirproof(models.AbstractModel):
    _inherit = 'theme.utils'

    @property
    def _header_templates(self):
        return ['theme_airproof.template_header_boxed_edit'] + super()._header_templates

    @property
    def _footer_templates(self):
        return ['theme_airproof.template_footer_contact_edit'] + super()._footer_templates

    def _theme_airproof_post_copy(self, mod):
        self.enable_view('theme_airproof.template_header_boxed_edit')
        self.enable_view('theme_airproof.template_footer_contact_edit')
