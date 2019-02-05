#!/bin/python

"""
    This script defines the functions specified at the README.md file for
    the Python code challenge.
"""

# importing dependencies
import random  # https://docs.python.org/3.6/library/random.html
import sqlite3  # https://docs.python.org/3.6/library/sqlite3.html
import string  # https://docs.python.org/3.6/library/string.html
import requests
import json

# Generate list of letters. Uppercase and lowercase letters
# have a 32 ascii shift for all letters.
lowercase_letters = [chr(i) for i in [j for j in range(ord('a'), ord('z') + 1)]]
uppercase_letters = [chr(i -32) for i in [j for j in range(ord('a'), ord('z') + 1)]]

# Generate list of digits.
digits = [chr(i) for i in [j for j in range(ord('0'), ord('9') + 1)]]

# List of punctuation charachers.
punctuation = [i for i in string.punctuation]

def generate_password(length = 5, complexity = 1):
    """
        Generate a random password with given length and complexity
        Complexity levels:
            Complexity == 1: return a password with only lowercase chars
            Complexity == 2: Previous level plus at least 1 digit
            Complexity == 3: Previous levels plus at least 1 uppercase char
            Complexity == 4: Previous levels plus at least 1 punctuation char

        Arg:
            length: number of characters
            complexity: complexity level

        Returns: generated password
    """

    # Generate password
    password_list = []
    if complexity >= 2 and (len(password_list) < length):
        password_list.append(random.choice(digits))
    if complexity >= 3 and (len(password_list) < length):
        password_list.append(random.choice(uppercase_letters))
    if complexity >= 4 and (len(password_list) < length):
        password_list.append(random.choice(punctuation))

    if (len(password_list) < length):
        for i in range(len(password_list), length):
            if complexity == 1:
                password_list.append(random.choice(lowercase_letters))
            elif complexity == 2:
                password_list.append(random.choice(lowercase_letters+digits))
            elif complexity == 3:
                password_list.append(random.choice(lowercase_letters+digits+uppercase_letters))
            elif complexity == 4:
                password_list.append(random.choice(lowercase_letters+digits+uppercase_letters+punctuation))

    # Convert list of characters in string with random order
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

def check_password_level(password):
    """Return the password complexity level for a given password

    Complexity levels:
        Return complexity 1: If password has only lowercase chars
        Return complexity 2: Previous level condition and at least 1 digit
        Return complexity 3: Previous levels condition and at least 1 uppercase char
        Return complexity 4: Previous levels condition and at least 1 punctuation

    Complexity level exceptions (override previous results):
        Return complexity 2: password has length >= 8 chars and only lowercase chars
        Return complexity 3: password has length >= 8 chars and only lowercase and digits

    Arg:
        password: password

    Returns: complexity level
    """

    password_list = [i for i in password]
    password_set = set(password_list)
    lowercase_letters_set = set(lowercase_letters)
    digits_set = set(digits)
    uppercase_letters_set = set(uppercase_letters)
    punctuation_set = set(punctuation)

    complexity = 1

    if len(digits_set.intersection(password_set)) > 0 or (len(password_list) >= 8 and password_set.issubset(lowercase_letters_set)):
        complexity = 2
    if len(uppercase_letters_set.intersection(password_set)) > 0 or (len(password_list) >= 8 and len(digits_set.intersection(password_set)) > 0 and password_set.issubset(lowercase_letters_set|digits_set)):
        complexity = 3
    if len(punctuation_set.intersection(password_set)) > 0:
        complexity = 4

    return complexity


def create_user(db_path = 'https://randomuser.me/api/?results=1'):  # you may want to use: http://docs.python-requests.org/en/master/
    """
        Retrieve a random user from https://randomuser.me/api/
        and persist the user (full name and email) into the given SQLite db

    Arg:
        db_path: path of the SQLite db file (to do: sqlite3.connect(db_path))

    Returns: None
    """
    resp = requests.get(db_path).json()
    first_name = resp['results'][0]['name']['first']
    last_name = resp['results'][0]['name']['last']
    full_name = first_name + ' ' + last_name
    email = resp['results'][0]['email']

    return full_name, email

if __name__ == '__main__':
    main()
