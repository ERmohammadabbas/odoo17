# __manifest__.py

{
    'name': 'Dynamic Cheques',
    'version': '17.1.0.0',
    'summary': 'Module for managing cheques and chequebooks',
    'sequence':-100,
    'description': """
        This module allows users to manage banks, chequebooks, and cheques.
    """,
    'author': 'Your Name',
    'website': 'http://www.odoo.com',
    'category': 'Accounting',
    'depends': ['base', 'account'],
    'data': [
        'views/bank_views.xml',
        'views/chequebook_views.xml',
        'views/cheque_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}



# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

