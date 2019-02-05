#!/bin/python

"""
Setup of database for random users.
"""

import sqlite3  # https://docs.python.org/3.6/library/sqlite3.html

con = sqlite3.connect('database.db')
cur = con.cursor()

sql_creation_script = """
    create table users(
        id integer not null primary key autoincrement,
        full_name text not null,
        email text not null,
        password text null
    )

"""
# cur.execute(sql_creation_script)

def db_insert(full_name, email, password):
    return """
        insert into users(full_name, email, password)
        values('{}', '{}', '{}')
    """.format(full_name, email, password)

# Data insertion will be as follows:
# cur.execute(db_insert('AAAAAA', 'aaamail.com', 'aaaaaa'))

con.commit()
con.close()
