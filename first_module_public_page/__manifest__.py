{
    'name': 'First Module Public Page',
    'version': '16.0.1.0.0',
    'category': 'Learning',
    'summary': 'Module for learning webpage abilities',
    'website': 'https://blog.yartsev.by',
    'author': 'yartsev',
    'depends': [
        'base',
        'web',
        'first_module',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/base_layout.xml',
        'views/first_model_public_list.xml',
        'views/first_model_public_item.xml',
    ],
    'assets': {
        'first_module_public_page.assets_first_module': [
            'first_module_public_page/static/src/scss/style.scss',
            'first_module_public_page/static/src/js/script.js',
        ],
    },
    
    'license': 'LGPL-3',
}