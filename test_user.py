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

if __name__ == "__main__":
    unittest.main()