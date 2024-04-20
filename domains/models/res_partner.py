from odoo import models, api 

from odoo.osv import expression


class Partner(models.Model):
    _inherit = "res.partner"

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        print("args", args)
        print("operator", operator)
        if self._context.get('first_model_partner_domain'):
            additional_domain = [
                "|", 
                    ("phone", "in", ["(803)-873-6126", "(334)-502-1024"]),
                    ("email", "in", ["azure.Interior24@example.com", "jackson.group82@example.com"]),
                
            ]
            domain = expression.AND([args or [], additional_domain])
            print("domain", domain)
            return super(Partner, self)._name_search(name=name, args=domain, operator=operator, limit=limit, name_get_uid=name_get_uid)
        return super(Partner, self)._name_search(name=name, args=args, operator=operator, limit=limit, name_get_uid=name_get_uid)
