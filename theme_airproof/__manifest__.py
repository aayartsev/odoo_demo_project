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
        'views/mega_menu_template.xml',
        'views/home_page_template.xml',
        'views/website_templates.xml',
        'views/404_temlpate.xml',
        'views/about_us_page.xml',
        'views/shapes_pages.xml',
        'data/images.xml',
        'data/presets.xml',
        'data/menu.xml',
        'data/ir_model.xml',
        'views/first_model_form_page.xml',
        'views/snippets/s_airproof.xml',
        'views/snippets/options.xml',
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
        'website.assets_wysiwyg': [
            'theme_airproof/static/src/snippets/s_airproof/options.js'
        ],
    },
}
