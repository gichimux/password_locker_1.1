import unittest
from password import Credentials
import pyperclip

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
        test if the application can delete an application credentials object in credentials list
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials(2,2,"john","dribble.com", "y")
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials() #delete credentials
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_contact_exists(self):
        '''
        test to check if contact exists method works
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials(1,1,"john","dribble.com", "y")
        test_credentials.save_credentials()

        credentials_exists = Credentials.credentials_exists("dribble.com")
        
        self.assertTrue(credentials_exists)
        
    def test_find_contact_by_name(self):
        '''
        test to check if we can find an application credential by name and display data
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials(2,2,"john","dribble.com", "y")
        test_credentials.save_credentials()

        found_password = Credentials.find_by_app_name("dribble.com")

        self.assertEqual(found_password.app_password, test_credentials.app_password)

    def test_display_all_credentials(self):
        '''
        test if application can list all credentials saved
        '''
        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)

    def test_copy_password(self):
        '''
        test to confirm that the application can copy the found password on the clipboard
        '''

        self.new_credentials.save_credentials()
        Credentials.copy_password("medium.com")

        self.assertEqual(self.new_credentials.app_password,pyperclip.paste())

if __name__ == "__main__":
    unittest.main()