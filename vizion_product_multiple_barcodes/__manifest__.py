{
    "name": "Product Multiple Barcodes",
    "version": "18.0.1.0.0",
    "author": "Vizion Tools",
    "website": "https://viziontools.com/",
    "license": "LGPL-3",
    "installable": True,
    "images": ["static/description/main_banner.png"],
    "summary": "Allows to define multiple additional barcodes for products and to search products by additional barcodes and internal reference.",
    "depends": [
        "product",
        "sale",
        "purchase",
        "stock",
    ],
    "data": [
        "security/ir.model.access.csv",
        "wizard/multiply_barcode_wizard.xml",
        "views/product_template_views.xml",
        "views/stock_picking_views.xml",
    ],
}
