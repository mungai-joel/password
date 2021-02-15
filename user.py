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
        
    