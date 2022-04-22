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
