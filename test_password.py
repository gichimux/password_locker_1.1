import unittest
from password import Credentials
class TestCredentials(unittest.TestCase):
    '''
    main test class for the credentials class
    '''
    def setUp(self):
        '''
        runs before every test
        '''
        
        self.new_user = Credentials(1,"jane","doe")
    
    def test_init(self):
        '''
        test if pbject is instantiated correctly
        '''
        self.assertEqual(self.new_user.id, 1)
        self.assertEqual(self.new_user.first_name, "jane")
        self.assertEqual(self.new_user.last_name, "doe")

if __name__ == "__main__":
    unittest.main()