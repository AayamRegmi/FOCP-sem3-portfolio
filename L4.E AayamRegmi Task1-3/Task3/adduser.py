from utilities_essentials import *
from password_string import en_dcode
import getpass

def add_user(username, real_name, password):
    '''Adds a new user to the file.

    Parameters:
        username (str): The username of the new user.
        real_name (str): The real name of the new user.
        password (str): The password of the new user.
    '''

    if check_exist(username) == True:
          print("Cannot add user\nReason: User already exists")
     
    else:
         encoded_password = en_dcode(password, 'encode')

         with open(password_file, 'a') as savefile:
              save_user = f"{username.lower()}:{real_name}:{encoded_password}"
              savefile.write('\n' + save_user)
         
         print("User sucessfully Created.")

username =         input("Enter your username  : ")
real_name =        input("Enter your realname  : ")

password =         getpass.getpass("Enter your password  : ")
confirm_password = getpass.getpass("Confirm your password: ")

if password == confirm_password:
     add_user(username, real_name, password)
else:
     print("Password doesnot match")
