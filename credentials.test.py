import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    def setUp(self):
        """
            Setup method for the test
        """
        self.new_credentials = Credentials(
            "Telegram", "developerTelegram", "myPass@2003")
        def test_init(self):
            """
           Test to check if the credentials object is created
        """
        self.assertEqual(self.new_credentials.account_platform, "Telegram")
        self.assertEqual(
            self.new_credentials.user_account_username, "developerTelegram")
        self.assertEqual(
            self.new_credentials.user_account_password, "myPass@2003")
        def test_save_credentials(self):
            """
        check whether the credentials object is saved to the user_credentials[]
        """
        self.assertEqual(len(Credentials.user_credentials), 0)
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.user_credentials), 1)



