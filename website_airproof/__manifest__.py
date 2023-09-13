{
    'name': 'Airproof Theme',
    'description': '...',
    'category': 'Website/Theme', # Обязательное условие для того, чтобы модуль распознавался как тема
    'version': '16.0.1.0.0',
    'website': 'https://blog.yartsev.by',
    'author': 'yartsev',
    'license': 'LGPL-3',
    'depends': ['web','website'],
    'data': [
        #
    ],
    'assets': {
        'web._assets_primary_variables': [
            ('website_airproof/static/src/scss/primary_variables.scss'),
        ],
        'web._assets_frontend_helpers': [
            ('website_airproof/static/src/scss/bootstrap_overridden.scss'),
        ],
        'web.assets_frontend': [
            # 'website_airproof/static/src/scss/theme.scss',
            'website_airproof/static/src/scss/font.scss',
            'website_airproof/static/src/js/theme.js',
        ],
    },
}
