#!/bin/python

"""
    Definitions for the class users.
"""

class User:
    """
        Class user. It's objects will be inserted in the database.
    """

    def __init__(self, full_name, email, password):
        self.full_name = full_name
        self.email = email
        self.password = password

    def get_full_name(self):
        return self.full_name

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def set_full_name(self, full_name):
        self.full_name = full_name

    def set_full_name(self, email):
        self.email = email

    def set_full_name(self):
        self.password = password
