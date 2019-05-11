from models import Credentials, User
import string, random, time

#function that creates new user account
def new_user(fname,lname,user_name,login_password):
    new_user = User(fname, lname, user_name, login_password)
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






