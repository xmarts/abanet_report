# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Reporte Xmarts',
    'summary': ' Adaptaciones a la plantilla box de odoo 11',

    'description': """
    - Adaptaciones a la plantilla box de odoo 11, Adecuacion al reporte de pago
    """,
    'author': "Xmarts",
    'website': "http://www.xmarts.com",
    'depends': ['base','sale','purchase','stock','contacts'],
    'data': [
        'views/templates.xml',
        'reports/report_invoice.xml',
        'reports/payment_receipt.xml'
    ]
}
