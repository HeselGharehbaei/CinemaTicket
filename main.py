from user import User, UserType
from bank_account import BankAccount
import os


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
    elif key == 19:
        name= input("Name:")
        last_name= input("Last Name:")
        owner= name+last_name
        password= input("Password:")
        balance= input("Balance:")
        return owner, balance, password
    elif key == 20:
        account_number= input("Account number:")
        return account_number
    elif key == 21:
        amount= input("Amount:")
        banck_account_password= input("Password:")
        cvv2= input("Cvv2:")       
        return  amount, banck_account_password, cvv2
    elif key == 22:
        destination_account_number= input("Destination account number:")
        return destination_account_number


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
                    User(username, password, birthday, phone_number)
                elif key == "5":  
                    os.system("clear")
                    user_type, username, password = receive_information(5) 
                    if user_type == '1':
                        user_type = UserType.MANAGER
                    elif user_type == '2':
                        user_type = UserType.NORMAL_USER                         
                    if User.sign_in(username, password, user_type):
                        while True:
                            key = input("According to the requested operation,"
                            " enter one of the following options:\n"
                            "---------------------------------------\n"
                            "7 ---> Profile\n"
                            "---------------------------------------\n"    
                            "8 ---> Movie list\n"
                            "---------------------------------------\n" 
                            "9 ---> Charge wallet\n"
                            "---------------------------------------\n"
                            "10 ---> Buy subscription\n"
                            "---------------------------------------\n"
                            "11 ---> Buy movie\n"
                            "---------------------------------------\n" 
                            "12 ---> Back\n"
                            "---------------------------------------\n"
                            "key:")               
                            if key == "7":
                                os.system("clear")
                                while True:
                                    try:
                                        key = input("According to the requested operation,"
                                        " enter one of the following options:\n"
                                        "---------------------------------------\n"
                                        "13 ---> View profile\n"
                                        "---------------------------------------\n"    
                                        "14 ---> Edit profile\n"
                                        "---------------------------------------\n" 
                                        "15 ---> Back to main menu\n"
                                        "---------------------------------------\n"
                                        "key:") 
                                        if key == "13":
                                            os.system("clear")
                                            print(User.sign_in(username, password, user_type))
                                        elif key == "14":
                                            os.system("clear")
                                            while True:
                                                try:
                                                    key = input("According to the requested operation,"
                                                    " enter one of the following options:\n"
                                                    "---------------------------------------\n"
                                                    "16 ---> Edit username \n"
                                                    "---------------------------------------\n"    
                                                    "17 ---> Edit phone_number\n"
                                                    "---------------------------------------\n" 
                                                    "18 ---> Edit password\n"
                                                    "---------------------------------------\n"
                                                    "19 ---> Back to profile \n" 
                                                    "---------------------------------------\n" 
                                                    "key:")                                             
                                                    if key == "16":
                                                        os.system("clear")
                                                        new_username = receive_information(16)
                                                        User.change_username(username, new_username)
                                                        username = new_username
                                                    elif key == "17":
                                                        os.system("clear")
                                                        new_phone_number = receive_information(17)
                                                        User.change_phone_number(username, new_phone_number)
                                                    elif key == "18":
                                                        os.system("clear")
                                                        password, new_password, repeat_new_password = receive_information(18)
                                                        if User.valid_new_password(new_password, repeat_new_password):
                                                            User.update_password(password, username, new_password)
                                                            password= new_password  
                                                        else:
                                                            continue 
                                                    elif key == "19":
                                                        os.system("clear")
                                                        break 
                                                except BaseException as e:
                                                    print(str(e))    
                                        elif key == "15":
                                            os.system("clear")
                                            break
                                    except BaseException as e:
                                        print(str(e))                          
                            elif key == "8":
                                os.system("clear")
                                pass
                            elif key == "9":
                                pass
                            elif key == "10":
                                os.system("clear")
                                pass
                            elif key == "11":
                                pass                                  
                            elif key == "12":
                                os.system("clear") 
                                break           
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
                "15 ---> Create account\n"
                "---------------------------------------\n" 
                "16 ---> My account\n"
                "---------------------------------------\n"  
                "17 ---> Back to main menu\n" 
                "---------------------------------------\n"                     
                "key:")
                if key == "15":
                    os.system("clear")
                    owner, balance, password= receive_information(19)
                    k= BankAccount(owner, balance, password)
                elif key == "16":
                    os.system("clear")
                    account_number= receive_information(20)  
                    user_banck_accoun= BankAccount.get_account(account_number)                          
                    while True:
                        key = input(f"According to the requested operation,"
                        " enter one of the following options:\n"
                        "---------------------------------------\n"    
                        "18 ---> Deposit\n"
                        "---------------------------------------\n"  
                        "19 ---> View balance\n"
                        "---------------------------------------\n"
                        "20 ---> Withdrawal\n"
                        "---------------------------------------\n"
                        "21 ---> Transfer\n"
                        "---------------------------------------\n"
                        "22 ---> Back to bank menu\n" 
                        "---------------------------------------\n"                       
                        "key:")
                        if key == "18":
                            os.system("clear")
                            amount, banck_account_password, cvv2= receive_information(21) 
                            if user_banck_accoun.check_infoـvalidation(cvv2, banck_account_password):
                                user_banck_accoun.__add__(float(amount))
                            else:
                                continue
                        elif key == "19":
                            os.system("clear")
                            print(user_banck_accoun)
                        elif key == "20":
                            os.system("clear")
                            amount, banck_account_password, cvv2= receive_information(21) 
                            if user_banck_accoun.check_infoـvalidation(cvv2, banck_account_password):
                                BankAccount.__sub__(float(amount))
                            else:
                                continue
                        elif key == "21":
                            os.system("clear")
                            destination_account_number= receive_information(22)
                            amount, banck_account_password, cvv2= receive_information(21) 
                            destination_account= BankAccount.get_account(destination_account_number)                                      
                            if user_banck_accoun.check_infoـvalidation(cvv2, banck_account_password):
                                user_banck_accoun.transfer(destination_account, float(amount))
                            else:
                                continue
                        elif key == "22":
                            os.system("clear")
                            break
                elif key == "17":
                    os.system("clear")
                    break
            except BaseException as e:
                print(str(e))                 
    if key== "3":
        break
