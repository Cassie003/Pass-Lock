import  random
import string
class Credentials():
    
    user_credentials = []

    def __init__(self, account_platform, user_account_username, user_account_password):
        """
            account_platform: New credentials account name eg pintrest account.
            user_account_password: New credentials account password.
        """
        self.account_platform = account_platform
        self.user_account_username = user_account_username
        self.user_account_password = user_account_password

    def save_credentials(self):
        """
            save credentials method that saves credentials into user_credentials[]
            @classmethod
    def find_by_account_platform(cls, account_platform):
        """
            Method that takes in a account_platform and returns a credentials that matches that account_platform.
        """
        for credentials in cls.user_credentials:
            if credentials.account_platform == account_platform:
                return credentials
        return False

"""
        Credentials.user_credentials.append(self)
        """
            deletes saved credential from the user_credentials[]
        """
        
