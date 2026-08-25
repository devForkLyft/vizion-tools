# -*- coding: utf-8 -*-
{
    'name': 'License & Document Flow',
    'version': '18.0.1.2.0',
    'category': 'Contacts',
    'summary': 'Store retail, wholesale & tax ID licenses with files, '
               'expiry dates and a unique customer ID on every contact, '
               'synced to Point of Sale.',
    'description': '''
License & Document Flow for Contacts
====================================

Add retail licenses, wholesale licenses, tax ID documents, expiry dates and a
unique customer ID directly on the contact form. Upload the supporting file for
each license and keep everything on the customer record. Key license fields are
also loaded into Point of Sale so cashiers can see them at the till.

Fields added to Contacts:

* Retail License number + file, with an expiry date
* Wholesale License 1, 2 and 3, each with its own file
* Tax ID file with its own expiry date
* Customer Unique ID / Number

The most important license details are pushed to the POS partner loader so they
are available inside Point of Sale.
''',
    'author': 'Vizion Tools',
    'website': 'https://viziontools.com',
    'support': 'support@viziontools.com',
    'license': 'AGPL-3',
    'depends': [
        'base', 'vizion_msa_report', 'point_of_sale',
    ],
    'data': [
        'views/partner_views.xml',
    ],
    'images': [
        'static/description/main_screenshot.png',
        'static/description/screenshot_1.png',
        'static/description/screenshot_2.png',
    ],
    'application': True,
    'installable': True,
}
