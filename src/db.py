from sqlite3 import connect
from os import environ, system

db = 'elokuvat_test' if 'PYTEST_VERSION' in environ else 'elokuvat'

connection = connect(f'{db}.db')

def clear():
    system(f'cat schema.sql | sqlite3 {db}.db')
