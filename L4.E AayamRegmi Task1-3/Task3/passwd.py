from utilities_essentials import *
from password_string import en_dcode
import getpass


def change_password(username, password, new_password):
    '''Changes the password of a user in the file.

    Parameters:
        username (str): The username of the user whose password needs to be changed.
        password (str): The current password of the user.
        new_password (str): The new password for the user.
    '''

    matched_password = False
    
    if check_exist(username) == True:
         user_details = read_file(password_file)
         
         for index, line in enumerate(user_details): #using enumerate to also aquire the index of the line
              
              if username == line[0] and password == en_dcode(line[2],'decode'):
                   matched_password = True
                   user_details[index][2] = en_dcode(new_password, 'encode') #using the index to change to new password
                   
                   
                   user_details_save = [":".join(map(str, lines)) for lines in user_details]
          
                   with open(password_file, 'w') as savefile:
                        savefile.write('\n'.join(user_details_save))
                        print("Password successfully changed")         

    elif matched_password == False:
         print("Cannot change passowrd\nPassword doesnot match")
         
    else:
          print("Cannot change password\nReason: User doesnot exist")          

username = input("Username: ")
password = getpass.getpass("Password: ")
new_password = getpass.getpass("New password: ")
confirm_new_password = getpass.getpass("Confirm password: ")

if new_password == confirm_new_password:
     change_password(username,password,new_password)
else:
     print("New password doesnot match")