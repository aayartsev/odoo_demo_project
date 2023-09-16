{
    'name': 'Airproof Theme',
    'description': '...',
    'category': 'Theme', # Обязательное условие для того, чтобы модуль распознавался как тема
    'version': '16.0.1.0.0',
    'website': 'https://blog.yartsev.by',
    'author': 'yartsev',
    'license': 'LGPL-3',
    'depends': ['website'],
    'data': [
        'views/header_templates.xml',
        'views/footer_templates.xml',
        'views/website_templates.xml',
        'data/images.xml',
        'data/presets.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            ('theme_airproof/static/src/scss/primary_variables.scss'),
        ],
        'web._assets_frontend_helpers': [
            ('theme_airproof/static/src/scss/bootstrap_overridden.scss'),
        ],
        'web.assets_frontend': [
            # 'website_airproof/static/src/scss/theme.scss',
            'theme_airproof/static/src/scss/font.scss',
            'theme_airproof/static/src/scss/header.scss',
            'theme_airproof/static/src/js/theme.js',
        ],
    },
}
