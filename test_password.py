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
        
        self.new_credentials = Credentials(1,1,"jane","medium.com", "x")
    
    def test_init(self):
        '''
        test if object is instantiated correctly
        '''
        self.assertEqual(self.new_credentials.user_id, 1)
        self.assertEqual(self.new_credentials.credentials_id, 1)
        self.assertEqual(self.new_credentials.user_name, "jane")
        self.assertEqual(self.new_credentials.app_name, "medium.com")
        self.assertEqual(self.new_credentials.app_password, "x")

    def test_save_credentials(self):
        
        '''
        Test if credentials are saved in the credentials list
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
    
    def tearDown(self):
        '''
        teardown method to clean up after test runs
        '''
        Credentials.credentials_list = []
    
    #test cases for class methods    
    def test_multiple_credentials(self):
        '''
        test to check if the program can save multiple credentials object in the credentials_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials(2,2,"john","dribble.com", "y")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credential(self):
        '''
        test if the application can delete a credentials object in credentials list
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials(2,2,"john","dribble.com", "y")
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials() #delete credentials
        self.assertEqual(len(Credentials.credentials_list),1)

if __name__ == "__main__":
    unittest.main()