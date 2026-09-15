import getpass

def get_flag():
    correct_password = 'password123'
    flag = 'CTF{your_flag_here}'

    password = getpass.getpass('Enter the password: ')
    if password == correct_password:
        print('Access granted.')
        print('Here is your flag:', flag)
    else:
        print('Access denied.')

if __name__ == "__main__":
    get_flag()

