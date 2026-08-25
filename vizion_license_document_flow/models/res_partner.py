from odoo import fields, models, api, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    retail_license_file = fields.Binary(string='Retail License File')
    retail_license = fields.Char(string='Retail License')
    wholesale_licence_file1 = fields.Binary(string='Wholesale License File1')
    wholesale_licence1 = fields.Char(string='Wholesale License 1')
    wholesale_licence_file2 = fields.Binary(string='Wholesale License File2')
    wholesale_licence2 = fields.Char(string='Wholesale License 2')
    wholesale_licence_file3 = fields.Binary(string='Wholesale License File3')
    wholesale_licence3 = fields.Char(string='Wholesale License 3')
    expiry_date = fields.Date(string='Expiry Date', help="for Retail License")
    customer_unique_id = fields.Char(string='Customer Unique ID/Number')
    tax_id_file = fields.Binary(string='Tax ID File')
    tax_id_expiry_date = fields.Date(string='Expiry Date', help="for Tax Id")

    @api.model
    def create_from_ui(self, partner):
        if partner.get('retail_license_file'):
            partner['retail_license_file'] = partner.get('retail_license_file').encode('utf-8')
        res = super(ResPartner, self).create_from_ui(partner)
        return res