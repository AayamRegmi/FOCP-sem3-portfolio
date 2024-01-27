import codecs

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