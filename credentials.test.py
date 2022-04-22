import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    def setUp(self):
        """
            Setup method for the test
        """
        self.new_credentials = Credentials(
            "Telegram", "developerTelegram", "myPass@2003")
