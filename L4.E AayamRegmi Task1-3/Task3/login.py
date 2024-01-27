from utilities_essentials import *
from password_string import en_dcode
import getpass

def login(username, password):
     '''Logs in a user by checking the credentials in the file.

    Parameters:
        username (str): The username of the user.
        password (str): The password of the user.

    Returns:
        bool: True if login is successful, False otherwise.
    '''
     user_details = read_file(password_file)
     login_successful = False
     
     for line in user_details:
          if username.lower() == line[0] and password == en_dcode(line[2],'decode'): #using .lower() to make sure username is always in small letter
               print(f"Successfully logged in, Welcome {username}")
               login_successful = True
               break
     
     if login_successful == False:
          print("cannot login\nReason:Credentials donot match")

username = input("Username: ")
password = getpass.getpass("Password: ")
login(username, password)
