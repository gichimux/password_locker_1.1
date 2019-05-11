import unittest
from password import Credentials

class TestCredentials(unittest.TestCase):
    '''
    main test class for the credentials class
    '''
    def setUp(self):
        '''
        Method that creates instances of class for testing
        '''
        
        self.new_credentials = Credentials(1,1,"jane","medium.com", '1234')
    
    def test_init(self):
        '''
        test if object is instantiated correctly
        '''
        self.assertEqual(self.new_credentials.user_id, 1)
        self.assertEqual(self.new_credentials.credentials_id, 1)
        self.assertEqual(self.new_credentials.user_name, "jane")
        self.assertEqual(self.new_credentials.app_name, "medium.com")
        self.assertEqual(self.new_credentials.app_password, "1234")

    def test_save_credentials(self):
        
        '''
        Test if credentials are saved in the credentials list
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

if __name__ == "__main__":
    unittest.main()