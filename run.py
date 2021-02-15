from user import User

def create_user(fname,lname,phone,email,password):
    '''
    Function to create a  new user

    '''
    new_user = User(fname,lname,phone,email,password)
    return new_user

def save_users (user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user (user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_user(number):
    '''
    Function that finds a user by number and returns the user

    '''
    return User.find_by_number(number)

def check_existing_users(number):
    '''
    function that checks if a user exists using number
    
    '''
    return User.user_exist(number)

def display_users():
    '''
    Function that returns all the saved users

    '''
    return User.display_users()

def main():
    print("Hello welcome to your user list. what is your name?")
    user_name = input()
    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True

        list = ('''
        create new account
        display accounts
        search for accounts
        exit password
        ''')

        print (list)
        print("use these short codes")
