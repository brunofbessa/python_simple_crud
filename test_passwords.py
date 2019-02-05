#!/bin/python

"""
   Tests for the methods.
"""

import unittest
import passwords

class TestPassword(unittest.TestCase):
    """
        aaa

    """

    def test_generate_password(self):
        """
            Teste of generate_password functionfrom passwords.
        """
        self.assertIsNotNone(passwords.generate_password(5, 1), 'Password generated is None.')


    def test_check_password_level(self):
        """
            Teste of check_password_level function from passwords.
        """
        self.assertEqual(passwords.check_password_level('abcde'), 1, 'Password complexity not equal to 1.')
        self.assertEqual(passwords.check_password_level('abcd0'), 2, 'Password complexity not equal to 2.')
        self.assertEqual(passwords.check_password_level('Abcd0'), 3, 'Password complexity not equal to 3.')
        self.assertEqual(passwords.check_password_level('A!cd0'), 4, 'Password complexity not equal to 4.')
        self.assertEqual(passwords.check_password_level('abcdefgh'), 2, 'Password complexity not equal to 2.')
        self.assertEqual(passwords.check_password_level('abcdefg8'), 3, 'Password complexity not equal to 3.')

    def test_create_user(self):
        """
            Teste of create_user function from passwords.
        """
        pass

if __name__ == '__main__':
    unittest.main()
