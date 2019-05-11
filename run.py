from models import Credentials, User
import string, random, time

#function that creates new user account
def new_user(user_name,login_password):
    new_user = User(user_name, login_password)
    return new_user

#function that saves the new user account to user list
def create_account(user):
    user.create_user()

#function to authenticate user account
def authenticate(user_name,login_password):
    return User.auth_user(user_name, login_password)

#function that creates new credentials objects
def new_credentials(user_name, app_name, app_password):
    new_credentials = Credentials(user_name, app_name, app_password)
    return new_credentials

#function that returns user's requested credentials
def display_credentials(name):
    return Credentials.find_by_app_name(name)

#function to confirm if users credentials are saved in list
def find_credentials(name):
    return Credentials.credentials_exists

#function that optionally generates passwords for users
def password_generator(length):
    password_list = []
    counter =1
    while counter <= length:
        gen_password = random.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase)
        password_list.append(gen_password)
        counter+=1
    return "".join(password_list)

#function to copy password to clipboard
def copy_password(name):
    Credentials.copy_password(name)

def main():
    '''
    The main function
    '''
    print("\n")
    print("===============Password_locker_Version_1.1===============")
    print("*"*30)
    while True:
        #interface for new user account creation
        print("shortcode : functionality\n 'ca' : create your account\n 'ln' : log in \n 'ex' : exit" )
        shortcode = input().lower().strip()
        if shortcode == "ca":
            print("*"*8 + "Create Your Username"+"*"*8)
            user_name = str(input("Username:"))
            print("*"*8 +"Create Your Password:"+ "*"*8)
            login_password = str(input("Password:"))
            print("\n")
            
            create_account(new_user(user_name,login_password))

            print(f" Good news, {user_name} has been created! \n login to proceed:")
            print("="*20)

        #logging in interface
        elif shortcode == "ln":
            print("ENter your Username and Password to verify:")
            print("="*30)
            user_name = str(input("Username:"))
            login_password = str(input("Password:"))
            auth = authenticate(user_name,login_password)
            #throw error if username or password is incorrect
            if auth == False:
                print("\n")
                print("FATAL: Invalid Username or Password")
                print(">"*30)
            #log user in if username and password is True
            elif auth == True:
                print("\n")
                print(f"{auth.user_name} is logged in to Password Locker:")
                print("-"*20)
                while True:
                    print("shortcode : functionality \n 'ac' : Add Credentials \n 'vc' : View Credentials \n 'cp' : Copy Password \n 'lo' : Log Out ")
                        get_shortcode = str(input().lower())

                        #enable user to add credentials
                        if get_shortcode == 'ac':
                            print("Add the account credentials you want to store:")
                            print("-"*20)
                            app_name = str(input("Application Name:"))
                            user_name = str(input("Your Username For The Application"))
                            
                            #optional password generation for user
                            print("Input 'y' to autogenerate password and 'n' to input your own")
                            app_password = str(input("Password:"))





