from odoo import models, api

from odoo.addons.http_routing.models.ir_http import slug


class FirstModel(models.Model):
    _name = 'first.model'

    _inherit = [
        'first.model',
        'website.seo.metadata',
        'website.published.mixin',
        'website.searchable.mixin',
    ]

    @api.depends_context('lang')
    def _compute_website_url(self):
        super(FirstModel, self)._compute_website_url()
        for record in self:
            record.website_url = "/records/%s" % (slug(record))
