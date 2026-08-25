from odoo import fields, models, api, _


class PosSession(models.Model):

    _inherit = ['pos.session']

    def _loader_params_res_partner(self):
        params = super()._loader_params_res_partner()
        # Fields defined by this module are always safe to load into POS.
        additional_params = ['retail_license', 'tax_id_file', 'expiry_date', 'tax_id_expiry_date']
        # class_of_trade is provided by the optional MSA Report module (vizion_msa_report).
        # Only load it when that module is installed, so this app stays standalone and free.
        if 'class_of_trade' in self.env['res.partner']._fields:
            additional_params.append('class_of_trade')
        params['search_params']['fields'].extend(additional_params)
        return params
