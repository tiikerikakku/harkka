from sqlite3 import connect
from os import environ, system

DB = 'elokuvat_test' if 'PYTEST_VERSION' in environ else 'elokuvat'

connection = connect(f'{DB}.db')

def clear():
    '''clears db'''

    system(f'cat schema.sql | sqlite3 {DB}.db')
