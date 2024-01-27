import codecs
import os
import getpass
import sys

password_file='test.txt'

def clear_screen():
     #clears the screen
     os.system('cls')

def go_next():
     #to have a pause during loop
     input("\npress enter to go back")

def read_file(password_file):
    '''Reads user details from a file and returns a list of user information.

    Parameters:
        password_file (str): The name of the text file containing user details.

    Returns:
        list: A list of lists, where each inner list represents a user's details.
    '''

    user_details = []

    with open(password_file, 'r') as savefile:
            for line in savefile:
                line = line.strip().split(':') #to seperate the values using :
                user_details.append(line)
    
    return user_details        


def en_dcode(password, option):
    '''Uses codecs to encode and decode a string variable.

    Parameters:
        password (str): The variable to encode or decode.
        option (str): The operation to perform, either 'encode' or 'decode'.

    Returns:
        str: The encoded or decoded string.
        '''
     
    if option == 'encode':
          encoded_password = codecs.encode(password, 'rot_13')
          return encoded_password

    elif option == 'decode':
          decoded_password = codecs.decode(password, 'rot_13')
          return decoded_password
     

def check_exist(username):
    '''Checks if a user with a given username exists in the file.

    Parameters:
        username (str): The username to check.

    Returns:
        bool: True if the user exists, False otherwise.
    '''
    get_file = read_file(password_file)

    if any(username.lower() == user[0] for user in get_file):
    #if true user exist
         return True 
    
    else:
    #false means user doesnot exist
        return False
    
         
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
              savefile.write(save_user + '\n')
         
         print("User sucessfully Created.")


def del_user(username):
    '''Deletes a user from the file.

    Parameters:
        username (str): The username of the user to be deleted.
    '''
     
    if check_exist(username) == True: #if user exists start operation
          user_details = read_file(password_file)
          
          for line in user_details:
                if username == line[0]:
                    user_details.remove(line)
            
          user_details_save = [":".join(map(str, lines)) for lines in user_details]
          
          with open(password_file, 'w') as savefile:
                savefile.write('\n'.join(user_details_save))

          print("User Sucessfully deleted")         

    else:
          print("Cannot delete user\nReason: User doesnot exist")
                

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
                                    
                    
def main():
     clear_screen()

     while True:
         print(f"Welcome\n===========================")
         option =  input("1.Create new user\n2.Delete user\n3.change password\n4.login\n5.exit\nyour command:")

         if option == '1':
              clear_screen()
              print("Welcome, create new account\n")
              
              username = input("Enter your username: ")
              realname = input("\nEnter your realname: ")

              #get pass to hide the password input
              password = getpass.getpass("\nEnter your password: ")
              confirm_password = getpass.getpass("\nConfirm your password: ")

              if password == confirm_password:
                   add_user(username,realname,password)
              else:
                   print("Password doesnot match")
                   
              go_next()
              clear_screen()
                
         elif option == '2':
              clear_screen()
              print("Welcome\n")

              username = input("Enter your account username to delete: ")
              del_user(username)
              go_next()
              clear_screen()

         elif option == '3':
              clear_screen()
              print("Welcome, change your password\n")

              username = input("Enter your account username: ")
              password = getpass.getpass("Enter your password: ")
            
              #type password 2 times to make sure password matches the desired input
              new_password = getpass.getpass("Enter your new password: ")
              confirm_password = getpass.getpass("Confirm your new password: ")

              if new_password == confirm_password:
                   change_password(username,password,new_password)
                   go_next()
              else:
                   print("password doesnot match")
                   go_next()
              
              clear_screen()

         elif option == '4':
              clear_screen()
              print("Welcome, log into your account\n")

              username = input("Enter your username:")
              password = getpass.getpass("Enter your password")

              login(username, password)
              go_next()
              clear_screen()
         
         elif option == '5':
              exit()

         else:
              print("Enter a valid number\n")

main()          
     

     


         
          



