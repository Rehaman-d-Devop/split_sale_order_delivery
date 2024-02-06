{
    'name': "Split delivery for sale orders",
    'version': '1.0',
    'summary': 'Module for splitting delivery orders based on the delivery date in sale order lines',
    'depends': [
        'base',
        'stock',
        'sale'   
    ],
    'author': "Habiburehaman",
    'category': 'Extra Tools',
    'description': "Module for splitting delivery orders based on the delivery date in sale order lines", 
    'data': [
        'views/sale_order.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}