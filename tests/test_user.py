import pytest
from user import User
from utils import exceptions
import os
from movie import Movie


class TestUser:
    @pytest.fixture
    def setup(self):
        self.user_1= User('amane', '1234', '04/07/1368')
        self.user_2= User('faride', '124', '04/07/1368')
        self.user_3= User('hesel', '1234', '04-07-1368')
        self.user_4= User('amane', '1234', '21/07/1368')  

    @pytest.fixture
    def test_sign_up(self, setup):
        self.user_1.sign_up()
        assert os.path.isfile('data/users.pickle')
        yield "test_sign_up"
        self.user_1.delete_user(self.user_1.username) 
        assert 'amane' not in User.load_users_data()

    def test_sign_up_errors(self, setup, test_sign_up):
        with pytest.raises(exceptions.PasswordLengthError):
            self.user_2.sign_up()      
        with pytest.raises(exceptions.BirthdateInputFormatError):
            self.user_3.sign_up() 
        with pytest.raises(exceptions.DuplicateUsernameError):
            self.user_4.sign_up()             

    @pytest.fixture
    def test_sign_in(self, test_sign_up):   
        self.user= User.sign_in('amane', '1234', self.user_1.user_type) 
        assert isinstance(User.load_users_data()[self.user_1.username], User)

    def test_sign_in_errors(self, test_sign_up):   
        with pytest.raises(exceptions.AccessError): 
            User.sign_in('amane', '1234')    
        with pytest.raises(exceptions.InvalidPasswordError): 
            User.sign_in('amane', '1244', self.user_1.user_type)   
        with pytest.raises(exceptions.InvalidUsernameError): 
            User.sign_in('amaneh', '1234', self.user_1.user_type)      

    def test_show_informations(self, test_sign_in):   
        assert self.user.username=="amane"
        assert [self.user.birthday.year, self.user.birthday.month, self.user.birthday.day]== [1368, 7, 4]
        assert self.user.__str__()== f"name: amane\n id: {self.user_1.id}\n" \
       f"phone number: None\n birthday:1368-07-04\n" \
       f"join_date: {self.user_1.join_date}\n wallet: 0\n" \
       f"subscription: Bronze\n movie list: []"
        
    def  test_chang_username(self, test_sign_in):   
        self.user_1.change_username('reyhane')
        assert self.user_1.username == 'reyhane'
        assert 'amane' not in User.load_users_data()
        assert User.load_users_data()['reyhane']== self.user_1

    def  test_chang_phone_number(self, test_sign_in):   
        self.user_1.change_phone_number('09910902715')
        assert self.user_1.phone_number == '09910902715'
        assert self.user_1.load_users_data()[self.user_1.username].phone_number== '09910902715'      

    def  test_chang_password(self, test_sign_in):   
        self.user_1.update_password('1234','0987')
        assert self.user_1._User__password == '0987'
        assert self.user_1.load_users_data()[self.user_1.username]._User__password== '0987'    

    def  test_charge_wallet(self, test_sign_in):   
        self.user_1.charge_wallet(100000)
        assert self.user_1._wallet == 100000
        assert self.user_1.load_users_data()[self.user_1.username]._wallet== 100000             

    def test_buy_subscription(self, test_sign_in):
        self.user_1.buy_subscription('Silver')    
        assert self.user_1.subscription == 'Silver'
        assert self.user_1.load_users_data()[self.user_1.username].subscription== 'Silver'  

    def test_buy_subscription(self, test_sign_in):
        self.user_1.buy_subscription('Silver')    
        assert self.user_1.subscription == 'Silver'
        assert self.user_1.load_users_data()[self.user_1.username].subscription== 'Silver'  

    @pytest.fixture
    def setup_movie(self):
        self.movie= Movie('lord of rings', 'action', '15', 100000)

    def test_buy_movie(self,setup_movie ,test_sign_in):
        self.user_1.buy_movie(self.movie, self.movie.price)    
        assert self.user_1.movie_list == [self.movie]
        assert self.user_1.load_users_data()[self.user_1.username].movie_list[0].name== 'lord of rings'
