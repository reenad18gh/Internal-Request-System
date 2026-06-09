{
    'name': 'Internal Request System',
    'version': '1.0',
    'summary': 'Employee internal request workflow system',
    'author': 'Rinad Alghamdi',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/request_sequence.xml',
        'views/request_views.xml',
    ],
    'installable': True,
    'application': True,
}
