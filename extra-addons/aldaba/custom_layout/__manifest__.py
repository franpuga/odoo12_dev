# -*- coding: utf-8 -*-
{
    'name': "Módulo Informes Personalizados Aldaba",

    'summary': """
        Módulo de Gestión de Informes Personalizados y Comunes Aldaba S.L.""",

    'description': """
        Cabecera, Pie de Página...
    """,

    'author': "Aldaba Servicios Profesionales",
    'website': "http://www.aldaba.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Reporting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'report/custom_layout_header.xml',
        'report/custom_layout_footer.xml',
    ],
}