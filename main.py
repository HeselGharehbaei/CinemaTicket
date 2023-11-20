from user import User, UserType
import os


def receive_information(key):

    """
    This function receive users information
    including username password and phone number
    when the key value is "1" and return them
    """
    if key == 1:
        username = input("username: ")
        password = input("password: ")
        phone_number = input("phone number(optional): ")
        birthday = input("Enter your date of birth in the format dd/mm/yyyy: ")
        if phone_number == "":
            phone_number = None
        return  username, password, birthday, phone_number 
    elif key == 2:
        user_type = input("1 ----> MANAGER\n2 ----> NORMAL_USER\nEnter you user type:")
        username = input("username: ")
        password = input("password: ")        
        return  user_type, username, password
    elif key == 11:
        new_username = input("new username: ")   
        return  new_username
    elif key == 12:
        new_phone_number = input("new phone number: ") 
        if new_phone_number == "":
            new_phone_number = None
        return  new_phone_number
    elif  key == 13:
        password = input("password: ")
        new_password = input("new password: ") 
        repeat_new_password = input("repeat new password: ") 
        return  password, new_password, repeat_new_password 


while True:
    try:
        key = input("According to the requested operation,"
        " enter one of the following options:\n"
        "---------------------------------------\n"
        "1 ---> Sign up\n"
        "---------------------------------------\n"    
        "2 ---> Sign in\n"
        "---------------------------------------\n"    
        "3 ---> Exit\n"
        "---------------------------------------\n"    
        "key:")
        if key == "1":
            os.system("clear")
            username, password, birthday, phone_number = receive_information(1)
            User.sign_up(username, password, birthday, phone_number)
        elif key == "2":  
            os.system("clear")
            user_type, username, password = receive_information(2) 
            if user_type == '1':
                user_type = UserType.MANAGER
            elif user_type == '2':
                user_type = UserType.NORMAL_USER 
            if User.sign_in(username, password, user_type):
                while True:
                    key = input("According to the requested operation,"
                    " enter one of the following options:\n"
                    "---------------------------------------\n"
                    "4 ---> Profile\n"
                    "---------------------------------------\n"    
                    "5 ---> Bank menu\n"
                    "---------------------------------------\n" 
                    "6 ---> Cinema menu\n"
                    "---------------------------------------\n"
                    "7 ---> Sign out\n"
                    "---------------------------------------\n"  
                    "key:")               
                    if key == "4":
                        os.system("clear")
                        while True:
                            key = input("According to the requested operation,"
                            " enter one of the following options:\n"
                            "---------------------------------------\n"
                            "8 ---> View profile\n"
                            "---------------------------------------\n"    
                            "9 ---> Edit profile\n"
                            "---------------------------------------\n" 
                            "10 ---> Back to main menu\n"
                            "---------------------------------------\n"
                            "key:") 
                            if key == "8":
                                os.system("clear")
                                print(User.sign_in(username, password, user_type))
                            elif key == "9":
                                os.system("clear")
                                while True:
                                    try:
                                        key = input("According to the requested operation,"
                                        " enter one of the following options:\n"
                                        "---------------------------------------\n"
                                        "11 ---> Edit username \n"
                                        "---------------------------------------\n"    
                                        "12 ---> Edit phone_number\n"
                                        "---------------------------------------\n" 
                                        "13 ---> Edit password\n"
                                        "---------------------------------------\n"
                                        "14 ---> Back to profile \n" 
                                        "---------------------------------------\n" 
                                        "key:") 
                                    
                                        if key == "11":
                                            os.system("clear")
                                            new_username = receive_information(11)
                                            User.change_username (username, new_username)
                                            username = new_username
                                        elif key == "12":
                                            os.system("clear")
                                            new_phone_number = receive_information(12)
                                            User.change_phone_number(username, new_phone_number)
                                        elif key == "13":
                                            os.system("clear")
                                            password, new_password, repeat_new_password = receive_information(13)
                                            if User.valid_new_password(new_password, repeat_new_password):
                                                User.update_password(password, username, new_password)
                                                password= new_password  
                                            else:
                                                continue 
                                        elif key == "14":
                                            os.system("clear")
                                            break 
                                    except ValueError as e:
                                        print(str(e))    
                            elif key == "10":
                                os.system("clear")
                                break                    
                    if key == "5":
                        os.system("clear")
                        while True:
                            key = input("According to the requested operation,"
                            " enter one of the following options:\n"
                            "---------------------------------------\n"    
                            "15 ---> Create account\n"
                            "---------------------------------------\n" 
                            "16 ---> Deposit\n"
                            "---------------------------------------\n"  
                            "17 ---> View balance\n"
                            "---------------------------------------\n"
                            "18 ---> Withdrawal\n"
                            "---------------------------------------\n"
                            "19 ---> Transfer\n"
                            "---------------------------------------\n"
                            "20 ---> Back to main menu\n" 
                            "---------------------------------------\n"                       
                            "key:")
                            if key == "15":
                                pass
                            elif key == "16":
                                pass
                            elif key == "17":
                                pass
                            elif key == "18":
                                pass
                            elif key == "19":
                                pass
                            elif key == "20":
                                os.system("clear")
                                break
                    if key == "6":
                        os.system("clear")
                        while True:
                            key = input("According to the requested operation,"
                            " enter one of the following options:\n"
                            "---------------------------------------\n"
                            "21 ---> Movie list\n"
                            "---------------------------------------\n"    
                            "22 ---> Wallet\n"
                            "---------------------------------------\n" 
                            "23 ---> Buy subscription\n"
                            "---------------------------------------\n"  
                            "24 ---> Back to main menu\n" 
                            "---------------------------------------\n"                       
                            "key:")
                            if key == "21":
                                pass
                            if key == "22":
                                pass
                            if key == "23":
                                pass
                            if key == "24":
                                os.system("clear")
                                break
                    if key == "7":
                        os.system("clear")  
                        break 
        elif key == "3":
            os.system("clear")
            break            
    except ValueError as e:
        print(str(e)) 
                
