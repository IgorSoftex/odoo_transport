{
    'name': 'Transportation deliveries',
    'description': "Module for ordering of transport deliveries",
    'summary': "Odoo module for automation of transport deliveries",
    'version': '17.0.1.0.0',
    'category': 'Customizations',
    'license': 'LGPL-3',
    'website': 'https://odoo.school/',
    'author': 'Ihor Pastushenko',

    'depends': [
        'base',
    ],

    'external_dependencies': {
        'python': [],
    },

    'data': [
        'security/transport_deliveries_access_groups.xml',
        'security/transport_deliveries_rules.xml',
        'security/ir.model.access.csv',
        'views/transport_deliveries_menu.xml',
        'views/transport_deliveries_transport_views.xml',
        'views/transport_deliveries_transportation_category_views.xml',
        'views/transport_deliveries_vehicle_brand_views.xml',
        'views/transport_deliveries_carrier_views.xml',
        'views/transport_deliveries_carrier_contact_person_views.xml',
        'views/transport_deliveries_transport_order_views.xml',
    ],

    'demo': [
    'demo/vehicle_brand_demo_data.xml',
    'demo/transportation_category_demo_data.xml',
    'demo/transport_demo_data.xml',
    'demo/carrier_demo_data.xml',
    'demo/carrier_contact_person_demo_data.xml',
    'demo/transport_order_demo_data.xml',
    ],

    'installable': True,
    'auto_install': False,

    'images': [
        'static/description/banner.png',
        'static/description/icon.jpeg',
    ],
}
