#!/bin/python
import passwords
from User import *
import database
import random
import sqlite3  # https://docs.python.org/3.6/library/sqlite3.html

"""
   Tests for the methods.
"""

db_path = 'https://randomuser.me/api/?results=1'

created_users = []

# Creation of users shows log information
for i in range(0, 11):
    print(passwords.create_user(db_path))
    full_name = passwords.create_user(db_path)[0]
    email = passwords.create_user(db_path)[1]
    password = passwords.generate_password(random.randrange(6, 12), random.randrange(1, 4))
    print(full_name, email, password)

    new_user = User(full_name, email, password)
    print(new_user)
    created_users.append(new_user)
    print('--------------')


con = sqlite3.connect('database.db')
cur = con.cursor()
for i in created_users:
    cur.execute(database.db_insert(i.get_full_name(), i.get_email(), i.get_password()))

con.commit()
con.close()
