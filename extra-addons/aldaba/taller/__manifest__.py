# -*- coding: utf-8 -*-
{
    'name': "Gestión Taller Vehículos",

    'summary': """
        App Gestión Taller Reparación Mecánica de Vehículos""",

    'description': """
        Incluye Vehículos y Órdenes de Reparación
    """,

    'author': "Aldaba Servicios Profesionales",
    'website': "http://www.aldaba.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Gestión Vehiculo',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'data/data.xml',
        'security/ir.model.access.csv',
        'views/vehiculo_view.xml',
        'views/order_reparacion_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
