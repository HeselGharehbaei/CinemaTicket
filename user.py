from uuid import uuid4
from datetime import datetime
from enum import Enum
from utils import exceptions
import os
import pickle


class UserType(Enum):
    MANAGER = 1
    NORMAL_USER = 2


class User:  
    """
    This class is made to register users
    """
#-----------------------------------------------------------key = "1"-----------------------------------------------------------#    
    def __init__(self, username: str, password: str, 
                 birthday: str, phone_number= None, 
                 user_type= UserType.NORMAL_USER,
                 wallet=0, subscription= 'Bronze',
                 movie_list= []) -> str | None:
        """
        Initializing an instance of the User class
        """

        self.__password = password 
        self.phone_number = phone_number
        self.id = uuid4()
        self.username = username
        try:
            self.birthday = datetime.strptime(birthday, '%d/%m/%Y').date()
        except :
            raise exceptions.BirthdateInputFormatError
        self.user_type= user_type
        self.join_date = datetime.now().date() 
        self._wallet= wallet
        self.subscription= subscription
        self.movie_list= movie_list
        self.save_data()        


    def save_data(self):
        if not self.username_is_exsist(self.username):
            if self.password_is_valid(self.__password):
                users_data= self.users_data()
                users_data[self.username]= self
                self.save_edited_data(users_data)
            else:
                exceptions.PasswordLengthError       
        else:
            raise exceptions.DuplicateUsernameError
        

    @staticmethod
    def save_edited_data(users_data):
        with open('data/users.pickle', 'wb') as file:
            pickle.dump(users_data, file) 


    @staticmethod
    def users_data():
        file_path = 'data/users.pickle'
        if os.path.isfile(file_path): 
            with open(file_path, 'rb') as file:
                users_data = pickle.load(file)
        else:
            users_data = {}  
        return users_data 
    

    @classmethod
    def username_is_exsist(cls, username: str) -> bool:
        users_data= cls.users_data()
        if username in users_data:
            return True
        return False
    

    @staticmethod
    def password_is_valid(password: str) -> bool:   
        if len(password) >= 4:
            return True
        return False   
        
#-----------------------------------------------------------key = "2"-----------------------------------------------------------#
    @classmethod
    def sign_in(cls, username: str, password: str, user_type= None)-> object:

        """
        This function checks the condition that the username be unique
        And  ntered a valid password that belongs to the user we are entering.
        """
        users_data= cls.users_data()
        if cls.username_is_exsist(username):         
            if users_data[username].__password == password:
                if users_data[username].user_type == user_type:
                    return users_data[username]
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
        return f"name: {self.username}\n id: {self.id}\n" \
       f"phone number: {self.phone_number}\n birthday:{self.birthday}\n" \
       f"join_date: {self.join_date}\n wallet: {self._wallet}\n" \
       f"subscription: {self.subscription}\n movie list: {self.movie_list}"
       
#-----------------------------------------------------------key = "11"-----------------------------------------------------------#
   
    @classmethod
    def change_username(cls, username: str, new_username: str):

        """
        This function changes the username and phone number
        """  
        if not cls.username_is_exsist(new_username):
            users_data = cls.users_data()
            users_data[new_username] = users_data.pop(username)
            users_data[new_username].username = new_username
            cls.save_edited_data(users_data)                    
        else:
            raise exceptions.DuplicateUsernameError   

#-----------------------------------------------------------key = "12"-----------------------------------------------------------#   
    @classmethod
    def change_phone_number(cls, username: str, new_phone_number: str = None):

        """
        This function changes the username and phone number
        """  
        users_data = cls.users_data()
        users_data[username].phone_number = new_phone_number
        cls.save_edited_data(users_data)

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
        if users_data[username].__password == password:
            if cls.password_is_valid(new_password):
                users_data[username].__password = new_password
                cls.save_edited_data(users_data)  
            else:
                raise exceptions.PasswordLengthError 
        else:
            raise exceptions.InvalidPasswordError      


    @classmethod
    def charge_wallet(cls, amount:float):
        users_data = cls.users_data()    
        cls._wallet+= amount
        users_data[cls.username]._wallet= cls._wallet
        cls.save_edited_data(users_data)


    @classmethod
    def by_subscription(cls, type_subscription: str):
        users_data = cls.users_data()        
        users_data[cls.username].subscription= type_subscription
        cls.save_edited_data(users_data)  

    @classmethod
    def by_movie(cls, movie: object, movie_price: float):
        users_data = cls.users_data()
        users_data[cls.username].movie_list.append(movie)
        users_data[cls.username]._wallet-= movie_price
        cls.save_edited_data(users_data)  
