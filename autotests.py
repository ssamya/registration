import unittest
import main
import errors


class TestRegistration(unittest.TestCase):

    def test_registration(self):
        valid_dict = {"login": "misha", "email": "miss@gmail.com", "password": "misharegistr"}
        result = main.add_to_csv(valid_dict)
        self.assertTrue(result)

    def test_invalid_login(self):
        invalid_dict = {"login": "", "email": "miss@gmail.com", "password": "misharegistr"}
        with self.assertRaises(errors.EmptyLoginError):
            main.add_to_csv(invalid_dict)

    def test_invalid_email(self):
        invalid_dict = {"login": "misha", "email": "", "password": "misharegistr"}
        with self.assertRaises(errors.EmptyEmailError):
            main.add_to_csv(invalid_dict)

    def test_invalid_password(self):
        invalid_dict = {"login": "misha", "email": "miss@gmail.com", "password": "123"}
        result = main.add_to_csv(invalid_dict)
        self.assertFalse(result)

