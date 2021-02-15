import pyperclip 

class User:

    user_list = [] #empty use list

    def __init__(self,first_name,last_name,number,email,password):

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email
        self.password = password

        #init method up here

    def save_user(self):

        '''
        save user method saves user objects into user list
        
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        delete user method deletes a saved user from user list

        '''
        User.user_list.remove(self)

    @classmethod
    def find_by_number(cls.number):
        
        '''
        Method that checks if a user exists from the list 
        Args:
            number: phone number to search if it exists
        Returns :
            boolean: true or false
        '''
        for user in cls.user_list:
            if user.phone_number === number:
                return True

        return False

    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list

    @classmethod
    def copy_email(cls,number):
        user_found = User.find_by_number(number)
        pyperclip.copy(user_found.email)


    