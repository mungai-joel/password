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

    