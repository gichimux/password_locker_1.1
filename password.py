import pyperclip

class Credentials:
    
    credentials_list = [] #list that holds credentials data
    def add_password(self):
        '''
        Method that adds credentials to list 
        '''
        Credentials.credentials_list.append(self)

    '''
    the object that creates instances of credentials class
    Args:
        credentials data and their indices in the list database
    '''
    
    def __init__ (self, user_id, credentials_id, user_name, app_name, app_password):
        self.id = id
        self.user_id = user_id
        self.credentials_id = credentials_id
        self.user_name = user_name
        self.app_name = app_name
        self.app_password = app_password


    @classmethod
    def find_by_app_name(cls, name):
        '''
        Method that finds credentials in database by application name
        Args:
            name: the name of application requested by user
        returns:
            username and password of application provided
        '''
        for credentials in cls.credentials_list:
            if credentials.app_name  == name:
                return credentials

    @classmethod
    def display_credentials(cls):
        '''
        Method to display credentials data stored by user
        '''
        return cls.credentials_list
    
    @classmethod
    def credentials_exists(cls, name):
        '''
        Method that checks if application credentials exist in list database
        Args:
            app_name: application to search for in list database
        Returns:
            boolean; True or False if application exists

        '''
        for credentials in cls.credentials_list:
            if credentials.app_name == name:
                return True
            return False
   
    @classmethod
    def copy_password(cls, name):
        '''
        Method that copies app_password to clipboard using pyperclip
        Args:
            name: name of application provided by find_app_by_name method
        '''     
        password_found = Credentials.find_by_app_name(name)
        pyperclip.copy(password_found.app_password)
                
class User:
    #def __init__ (self)
    pass