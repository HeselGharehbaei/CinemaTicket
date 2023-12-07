from uuid import uuid4
from datetime import datetime
import json
from enum import Enum
from utils import exceptions


class UserType(Enum):
    MANAGER = 1
    NORMAL_USER = 2


class User:  

    """
    This class is made to register users
    """

    def __init__(self, username: str, password: str, birthday: str, phone_number= None, user_type= 'NORMAL_USER', id= None, join_date= None) -> str | None:
        """
        Initializing an instance of the User class
        """

        self.__password = password 
        self.phone_number = phone_number
        if id != None:
            self.id = id
        else:    
            self.id = str(uuid4())
        self.username = username
        try:
            self.birthday = datetime.strptime(birthday, '%d/%m/%Y').date()
        except :
            raise ValueError("The input format for birthday is wrong. Please try in the format dd/mm/yyyy.")  
        if join_date != None:
            self.join_date= datetime.strptime(join_date, '%d/%m/%Y').date()
        else:  
            self.join_date = datetime.now().date()
        if user_type == 'NORMAL_USER':
            self.user_type = UserType.NORMAL_USER
        elif user_type == 'MANAGER':
            self.user_type = UserType.MANAGER       


    @staticmethod
    def users_data():
        try: 
            with open('data/users.json', 'r') as file:
                users_data = json.load(file)
            return users_data
        except:
            users_data = {}
            return users_data
                    

    @classmethod
    def username_is_exsist_in_users_data_and_return(cls, username: str):
        if username in cls.users_data():
            return cls(**cls.users_data()[username])
        return False
    

    def to_dict(self):
        return{
            "username": self.username,
            "password": self.__password,
            "phone_number": self.phone_number,
            "birthday": self.birthday.strftime('%d/%m/%Y'),
            "id": self.id,
            "join_date": self.join_date.strftime('%d/%m/%Y'),  
            "user_type": self.user_type.name,     
        }


    @staticmethod
    def password_is_valid(password: str):   
        if len(password) >= 4:
            return True
        return False   
        
 #-----------------------------------------------------------key = "1"-----------------------------------------------------------#

    @classmethod
    def sign_up(cls, username: str, password: str, birthday:str, phone_number:str = None, user_type= 'NORMAL_USER')-> json:

        """
       This function is a classmethod and registers the user in the 
       user class after receiving the information
        """
        
        if not cls.username_is_exsist_in_users_data_and_return(username):
            if cls.password_is_valid(password): 
                new_user_account = cls(username, password, birthday, phone_number, user_type)
                users_data= cls.users_data()
                users_data[username]= new_user_account.to_dict()    
                with open('data/users.json', 'w') as file:
                    json.dump(users_data, file, indent=2)               
            else:
                raise exceptions.PasswordLengthError
        else:
            raise exceptions.DuplicateUsernameError


#-----------------------------------------------------------key = "2"-----------------------------------------------------------#


    @classmethod
    def sign_in(cls, username: str, password: str, user_type= None)-> object:

        """
        This function checks the condition that the username be unique
        And  ntered a valid password that belongs to the user we are entering.
        """
        the_username_data= cls.username_is_exsist_in_users_data_and_return(username)
        if the_username_data:         
            if the_username_data.__password == password:
                if the_username_data.user_type == user_type:
                    return the_username_data
                else:
                    raise exceptions.AccessError
            else:
                raise exceptions.InvalidPasswordError
        else:
            raise exceptions.InvalidUsernameError

#-----------------------------------------------------------key = "8"-----------------------------------------------------------#
   
    def __str__(self) -> str:
        """
        This function use to show user
        information in the special format
        """
        return f"name: {self.username}, id: {self.id}, phone number: {self.phone_number}, birthday:{self.birthday},join_date: {self.join_date}"


#-----------------------------------------------------------key = "11"-----------------------------------------------------------#
   
   
    @classmethod
    def change_username(cls ,username: str, new_username: str):

        """
        This function changes the username and phone number
        """  
        if not cls.username_is_exsist_in_users_data_and_return(new_username):
            users_data = cls.users_data()
            users_data[new_username] = users_data.pop(username)
            users_data[new_username]['username'] = new_username
            with open('data/users.json', 'w') as file:
                json.dump(users_data, file, indent=2)                       
        else:
            raise exceptions.DuplicateUsernameError   

#-----------------------------------------------------------key = "12"-----------------------------------------------------------#   
    
    @classmethod
    def change_phone_number(cls ,username: str, new_phone_number: str = None):

        """
        This function changes the username and phone number
        """  
        users_data = cls.users_data()
        users_data[username]['phone_number'] = new_phone_number
        with open('data/users.json', 'w') as file:
            json.dump(users_data, file, indent=2)
#-----------------------------------------------------------key = "13"-----------------------------------------------------------#
 
    @staticmethod
    def valid_new_password(new_password: str, repeat_new_password: str):

        """
        This function cheack the new password
        and repeated new password is equal toghether
        """
        if new_password == repeat_new_password:
            return True
        raise exceptions.MismatchOfPasswordsError 
    

    @classmethod
    def update_password(cls, password: str, username: str, new_password: str):

        """
        Replacing the new password with the previous password of a user
        """
        users_data = cls.users_data()
        if users_data[username]['password'] == password:
            if cls.password_is_valid(new_password):
                users_data[username]['password'] = new_password
                with open('data/users.json', 'w') as file:
                    json.dump(users_data, file, indent=2)    
            else:
                raise exceptions.PasswordLengthError 
        else:
            raise exceptions.InvalidPasswordError      
