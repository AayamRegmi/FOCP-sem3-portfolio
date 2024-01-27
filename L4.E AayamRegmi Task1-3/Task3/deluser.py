from utilities_essentials import *


def del_user(username):
    '''Deletes a user from the file.

    Parameters:
        username (str): The username of the user to be deleted.
    '''
     
    if check_exist(username.lower()) == True: #if user exists start operation
          user_details = read_file(password_file)
          
          for line in user_details:
                if username.lower() == line[0]:
                    user_details.remove(line)
            
          user_details_save = [":".join(map(str, lines)) for lines in user_details]
          
          with open(password_file, 'w') as savefile:
                savefile.write('\n'.join(user_details_save))

          print("User Sucessfully deleted")         

    else:
          print("Cannot delete user\nReason: User doesnot exist")

username = input("Enter username: ")
del_user(username)