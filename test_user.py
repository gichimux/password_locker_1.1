import unittest
from models import User
 
class TestUser(unittest.TestCase):
    '''
    main test for User class
    '''
    def setUp(self):
         '''
         Method that creates a user Object for testing
         '''
         self.new_user = User("cersei", "jon","cerjon", "x")

    def test_init(self):
        '''
        test if object is instantiated correctly
        '''
        self.assertEqual(self.new_user.fname, "cersei")
        self.assertEqual(self.new_user.lname, "jon")
        self.assertEqual(self.new_user.user_name, "cerjon")
        self.assertEqual(self.new_user.login_password, "x")

    def test_create_account(self):
        '''
        test to check if application adds user account to user_list
        '''
        User.user_list.append(self)

    def test_auth(self):
        '''
        test to check if application authetication works
        '''
        self.new_user.create_user()
        authenticate = User.auth_user("cerjon", "x")

        self.assertTrue(authenticate)

if __name__ == "__main__":
    unittest.main()