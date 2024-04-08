from user import User, UserType
from bank_account import BankAccount
import os
from movie import Movie
from reservation import Reservation

def receive_information(key):

    """
    This function receive users information
    including username password and phone number
    when the key value is "1" and return them
    """
    if key == 4:
        username = input("Username: ")
        password = input("Password: ")
        phone_number = input("Phone number(optional): ")
        birthday = input("Enter your date of birth in the format dd/mm/yyyy: ")
        if phone_number == "":
            phone_number = None
        return  username, password, birthday, phone_number 
    elif key == 5:
        user_type = input("1 ----> MANAGER\n2 ----> NORMAL_USER\nEnter user type:")
        username = input("Username: ")
        password = input("Password: ")        
        return  user_type, username, password
    elif key == 16:
        new_username = input("New username: ")   
        return  new_username
    elif key == 17:
        new_phone_number = input("New phone number: ") 
        if new_phone_number == "":
            new_phone_number = None
        return  new_phone_number
    elif  key == 18:
        password = input("Password: ")
        new_password = input("New password: ") 
        repeat_new_password = input("Repeat new password: ") 
        return  password, new_password, repeat_new_password 
    elif key == 20:
        name= input("Name:")
        last_name= input("Last Name:")
        owner= name+last_name
        password= input("Password:")
        balance= input("Balance:")
        return owner, balance, password
    elif key == 21:
        account_number= input("Account number:")
        return account_number
    elif key == 22:
        amount= float(input("Amount:"))
        banck_account_password= input("Password:")
        cvv2= input("Cvv2:")       
        return  amount, banck_account_password, cvv2
    elif key == 23:
        destination_account_number= input("Destination account number:")
        return destination_account_number
    elif key == 24:
        banck_account_password= input("Password:")
        cvv2= input("Cvv2:") 
        return  banck_account_password, cvv2


while True:
    key = input("According to the requested operation,"
        " enter one of the following options:\n"
        "---------------------------------------\n"
        "1 ---> Cinema Ticket menu\n"
        "---------------------------------------\n"    
        "2 ---> Bank menu\n"
        "---------------------------------------\n"    
        "3 ---> Exit\n"
        "---------------------------------------\n"    
        "key:")
    if key == "1":
        os.system("clear")
        while True:
            try:                                                
                key = input("According to the requested operation,"
                " enter one of the following options:\n"
                "---------------------------------------\n"
                "4 ---> Sign up\n"
                "---------------------------------------\n"    
                "5 ---> Sign in\n"
                "---------------------------------------\n"    
                "6 ---> Logout\n"
                "---------------------------------------\n"    
                "key:")
                if key == "4":
                    os.system("clear")
                    username, password, birthday, phone_number = receive_information(4)
                    User(username, password, birthday, phone_number).sign_up()
                elif key == "5":  
                    os.system("clear")
                    user_type, username, password = receive_information(5) 
                    if user_type == '1':
                        user_type = UserType.MANAGER
                    elif user_type == '2':
                        user_type = UserType.NORMAL_USER 
                    user= User.sign_in(username, password, user_type)                            
                    if user:
                        while True:
                            try:
                                key = input("According to the requested operation,"
                                " enter one of the following options:\n"
                                "---------------------------------------\n"
                                "7 ---> Profile\n"
                                "---------------------------------------\n"    
                                "8 ---> Movie list and Buy movie\n"
                                "---------------------------------------\n" 
                                "9 ---> Back\n"
                                "---------------------------------------\n"
                                "key:")               
                                if key == "7":
                                    os.system("clear")
                                    while True:
                                        try:
                                            key = input("According to the requested operation,"
                                            " enter one of the following options:\n"
                                            "---------------------------------------\n"
                                            "10 ---> View profile\n"
                                            "---------------------------------------\n"    
                                            "11 ---> Edit profile\n"
                                            "---------------------------------------\n" 
                                            "12 ---> Charge wallet\n"
                                            "---------------------------------------\n" 
                                            "13 ---> Buy subscription\n"
                                            "---------------------------------------\n"                                                                                 
                                            "14 ---> Back to main menu\n"
                                            "---------------------------------------\n"
                                            "key:") 
                                            if key == "10":
                                                os.system("clear")
                                                print(user)
                                            elif key == "11":
                                                os.system("clear")
                                                while True:
                                                    try:
                                                        key = input("According to the requested operation,"
                                                        " enter one of the following options:\n"
                                                        "---------------------------------------\n"
                                                        "15 ---> Edit username \n"
                                                        "---------------------------------------\n"    
                                                        "16 ---> Edit phone_number\n"
                                                        "---------------------------------------\n" 
                                                        "17 ---> Edit password\n"
                                                        "---------------------------------------\n"
                                                        "18 ---> Back to profile \n" 
                                                        "---------------------------------------\n" 
                                                        "key:")                                             
                                                        if key == "15":
                                                            os.system("clear")
                                                            new_username = receive_information(16)
                                                            user.change_username(new_username)
                                                        elif key == "16":
                                                            os.system("clear")
                                                            new_phone_number = receive_information(17)
                                                            user.change_phone_number(new_phone_number)
                                                        elif key == "17":
                                                            os.system("clear")
                                                            password, new_password, repeat_new_password = receive_information(18)
                                                            if user.valid_new_password(new_password, repeat_new_password):
                                                                user.update_password(password, new_password)
                                                                password= new_password  
                                                            else:
                                                                continue 
                                                        elif key == "18":
                                                            os.system("clear")
                                                            break 
                                                    except BaseException as e:
                                                        print(str(e)) 
                                            elif key == "12":
                                                os.system("clear")
                                                account_number= receive_information(21)  
                                                user_banck_accoun= BankAccount.get_account(account_number) 
                                                amount, banck_account_password, cvv2= receive_information(22) 
                                                if user_banck_accoun.check_infoـvalidation(cvv2, banck_account_password):
                                                    user_banck_accoun.__sub__(float(amount))
                                                    user.charge_wallet(amount)
                                                else:
                                                    continue
                                            elif key == "13":
                                                os.system("clear")
                                                key = input("1) Silver ---> 200000 Toman\n"
                                                            "---------------------------------------\n"
                                                            "2) Gold ---> 400000 Toman\n"
                                                            "---------------------------------------\n"
                                                            "3) Cancel\n"
                                                            "---------------------------------------\n"
                                                            "key:")
                                                type_subscription= ''
                                                amount= 0
                                                if key== 1:
                                                    type_subscription= 'Silver'
                                                    amount= 200000
                                                elif key== 2:
                                                    type_subscription= 'Gold'
                                                    amount= 400000  
                                                elif key ==3:  
                                                    break                                     
                                                account_number= receive_information(20)  
                                                user_banck_accoun= BankAccount.get_account(account_number) 
                                                banck_account_password, cvv2= receive_information(24) 
                                                if user_banck_accoun.check_infoـvalidation(cvv2, banck_account_password):
                                                    user_banck_accoun.__sub__(amount)
                                                    user.buy_subscription(type_subscription)
                                                else:
                                                    continue                                            
                                            elif key == "14":
                                                os.system("clear")
                                                break
                                        except BaseException as e:
                                            print(str(e))                          
                                elif key == "8":
                                    os.system("clear")
                                    movies= Movie.load_movies()
                                    movies_list= (list(movies.values()))
                                    [print(f"{movies_list.index(movie)}:",movie) for movie in movies_list]
                                    number_of_movie= input("Enter number of movie you want:")
                                    selected_movie= movies_list[int(number_of_movie)]
                                    reservation_list_of_the_movie= Reservation.load()[selected_movie.name]
                                    selected_movie_price= reservation_list_of_the_movie.final_price(user)
                                    print(f"movie_final_price: {selected_movie_price}")
                                    sure_for_movie_price_agreemant= input("If you sure from the movie's price Enter number 1 or not number 0:")
                                    if sure_for_movie_price_agreemant== "1" and user.check_wallet_balance(selected_movie_price):
                                        reservation_list_of_the_movie.make_reservation(user)                 
                                elif key == "9":
                                    os.system("clear") 
                                    break                           
                            except BaseException as e:
                                print(str(e))                 
                elif key == "6":
                    os.system("clear")
                    break    
            except BaseException as e:
                print(str(e))                                        
    if key == "2":
        os.system("clear")
        while True:
            try:
                key = input("According to the requested operation,"
                " enter one of the following options:\n"
                "---------------------------------------\n"    
                "19 ---> Create account\n"
                "---------------------------------------\n" 
                "20 ---> My account\n"
                "---------------------------------------\n"  
                "21 ---> Back to main menu\n" 
                "---------------------------------------\n"                     
                "key:")
                if key == "19":
                    os.system("clear")
                    owner, balance, password= receive_information(20)                    
                    BankAccount(owner, float(balance), password)
                elif key == "20":
                    os.system("clear")
                    account_number= receive_information(21)  
                    user_banck_accoun= BankAccount.get_account(account_number)                          
                    while True:
                        key = input(f"According to the requested operation,"
                        " enter one of the following options:\n"
                        "---------------------------------------\n"    
                        "22 ---> Deposit\n"
                        "---------------------------------------\n"  
                        "23 ---> View balance\n"
                        "---------------------------------------\n"
                        "24 ---> Withdrawal\n"
                        "---------------------------------------\n"
                        "25 ---> Transfer\n"
                        "---------------------------------------\n"
                        "26 ---> Back to bank menu\n" 
                        "---------------------------------------\n"                       
                        "key:")
                        if key == "22":
                            os.system("clear")
                            amount, banck_account_password, cvv2= receive_information(22) 
                            if user_banck_accoun.check_infoـvalidation(cvv2, banck_account_password):
                                user_banck_accoun.__add__(amount)
                            else:
                                continue
                        elif key == "23":
                            os.system("clear")
                            print(user_banck_accoun)
                        elif key == "24":
                            os.system("clear")
                            amount, banck_account_password, cvv2= receive_information(22) 
                            if user_banck_accoun.check_infoـvalidation(cvv2, banck_account_password):
                                user_banck_accoun.__sub__(float(amount))
                            else:
                                continue
                        elif key == "25":
                            os.system("clear")
                            destination_account_number= receive_information(23)
                            amount, banck_account_password, cvv2= receive_information(22) 
                            destination_account= BankAccount.get_account(destination_account_number)                                      
                            if user_banck_accoun.check_infoـvalidation(cvv2, banck_account_password):
                                user_banck_accoun.transfer(destination_account, float(amount))

                        elif key == "26":
                            os.system("clear")
                            break
                elif key == "21":
                    os.system("clear")
                    break
            except BaseException as e:
                print(str(e))                 
    if key== "3":
        break
