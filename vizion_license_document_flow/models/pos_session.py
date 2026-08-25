from odoo import fields, models, api, _


class PosSession(models.Model):

    _inherit = ['pos.session']

    def _loader_params_res_partner(self):
        params = super()._loader_params_res_partner()
        additional_params = ['class_of_trade', 'retail_license', 'tax_id_file', 'expiry_date', 'tax_id_expiry_date']
        params['search_params']['fields'].extend(additional_params)
        return params
