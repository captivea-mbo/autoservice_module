# -*- coding: utf-8 -*-
from . import autoservicescustomer

{
    'name': 'Mechanical Services and  Maintenance',
    'version': '12.0.0.0',
    'summary': """Module Auto Services""",
    'author': 'Marcos Bolivar',
    'category': 'Extra Tools',
    'depends': ['sale', 'mail', 'report_xlsx', 'web_timeline'],
    'data': [
        autoservicescustomer.xnl,
    ],
    'images': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}