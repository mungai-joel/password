from user import User

def create_user (fname,lname,phone,email,password):
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
        print("use these short codes : create new account  ,  display accounts  ,  search for accounts  ,  exit password  ")

        short_code = input().lower()

        if short_code == '1':
            print("New user")
            print("-"*10)

            print("First name ...")
            f_name = input()

            print ("Last name ...")
            l_name = input()

            print("phone number ...")
            p_number = input()

            print("Email address ...")
            e_address = input()

            print("password ...")
            password = input()

            print("confirm password ...")
            password = input()

            save_users(create_user(f_name,l_name,p_number,e_address,password))
            print('\n')
            print(f"New user {f_name} {l_name} created")
            print('\n')

        elif short_code == '2':

            if display_users():
                print("here is a list of all your users")
                print('\n')

            for user in display_users():

                print(f"{user.first_name} {user.last_name} {user.phone_number}")

                print('\n')

            else:
                print('\n')

                print('\n')

        elif short_code == '3':

            print("Enter the number to search for ")

            search_number = input()
            if check_existing_users(search_number):
                search_user = find_user(search_number)
                print(f"{search_user.first_name} {search_user.last_name}")
                print('-' * 20)

                print(f"phone number.........{search_user.phone_number}")
                print(f"Email address.........{search_user.email}")
            else:
                print("That user does not exist")


            elif short_code == "4":
                print
                ("bye ....")

                break
            else:
                print("I didnt get it, please use short codes ")

if __name__ == '__main__':
    main()



