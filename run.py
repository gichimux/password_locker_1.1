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
#function that saves password


