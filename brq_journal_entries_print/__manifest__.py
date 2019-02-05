# -*- encoding: UTF-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2015-Today Boraq Group - Business Solutions.
#    (<http://www.boraq-group.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################


{
    'name': 'Journal Entries Printing',
    'version': '11.0',
    'category': 'account',
    'sequence': 9,
    'summary': 'Journal Entries Printing',
    'description': """
    This module use for printing journal entries in PDF report."
    """,
    'author': "Boraq Group",
    'website': "http://www.boraq-group.com",
    'depends': ['account'],
    'license': 'AGPL-3',
    'data': [
            'report/report_menu.xml'
            ],
    "images": [
        'static/description/icon.png'
    ],
    'demo': [],
    'price': 00,
    'currency': 'USD',
    'installable': True,
    'auto_install': False,
}
