import  unittest
from    user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        """
        Setup method for the test class to create a new user
        """
        self.new_user = User("casey", "minu",
                             "developercasey", "k8ddj6m2l")
    def test_user_created(self):
        """
        Test to check if the user object is created
        """
        self.assertEqual(self.new_user.first_name, "casey")
        self.assertEqual(self.new_user.last_name, "minu")
        self.assertEqual(self.new_user.username, "developercasey")
        self.assertEqual(self.new_user.password, "k8ddj6m2l")

