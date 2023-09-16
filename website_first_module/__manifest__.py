{
    'name': 'Website and First Module',
    'version': '16.0.1.0.0',
    'category': 'Learning',
    'summary': 'Module for learning website module abilities',
    'website': 'https://blog.yartsev.by',
    'author': 'yartsev',
    'depends': [
        'website',
        'first_module',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/website_menu_data.xml',
        'views/first_model_templates.xml',
        'views/theme_selection_menu.xml',

    ],
    'demo': ['data/records_demo.xml', ],
    'assets': {
        'web.assets_frontend': [
            'website_first_module/static/src/js/user_custom_toggle_visible_record.js',
        ],
    },
    'installable': True, # ???
    'auto_install': True, # Модуль будет автоматически установлен, если все зависимости удовлетворены
    'license': 'LGPL-3',
}