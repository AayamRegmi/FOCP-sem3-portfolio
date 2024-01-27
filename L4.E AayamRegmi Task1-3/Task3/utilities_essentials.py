password_file = 'passwd.txt'

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
