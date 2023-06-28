{
    'name': 'First Module',
    'version': '16.0.1.0.0',
    'category': 'Learning',
    'summary': 'Module for learning',
    'website': 'https://blog.yartsev.by',
    'author': 'yartsev',
    'depends': [
        'base',
        'web',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/first_model.xml',
        'views/menus.xml',
        'views/print_form.xml',
    ],
    'demo': ['data/records_demo.xml', ],
    'license': 'LGPL-3',
}
