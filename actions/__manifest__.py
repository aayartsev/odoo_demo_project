{
    'name': 'Actions Example',
    'version': '16.0.1.0.0',
    'category': 'Learning',
    'summary': 'Module for learning',
    'website': 'https://blog.yartsev.by',
    'author': 'yartsev',
    'depends': [
        'first_module',
    ],
    'data': [
        'views/first_model.xml',
        'views/report_action.xml',
        'views/server_action.xml',
        'views/menus.xml',
        'views/first_model_report_template.xml',
    ],
    'assets': {'web.assets_backend': ['actions/static/src/js/client_action.js', ], },
    'demo': ['data/records_demo.xml', ],
    'license': 'LGPL-3',
}
