from sqlite3 import connect
from os import system

connection = connect('elokuvat.db')

def clear():
  system('cat schema.sql | sqlite3 elokuvat.db')
