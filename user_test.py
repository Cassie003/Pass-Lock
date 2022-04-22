import  unittest
from    user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        """
        Setup method for the test class to create a new user
        """
        self.new_user = User("casey", "minu",
                             "developercasey", "k8ddj6m2l")
