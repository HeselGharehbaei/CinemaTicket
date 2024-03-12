class BaseException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message= message

    def __str__(self) -> str:
        return   f'{self.message}' 
            

class MinBalanceError(BaseException):
    def __init__(self, message="balance can't be below 10000 tomans"):
        super().__init__(message)


class PasswordCvv2Error(BaseException):
    def __init__(self, message="Password or CVV2 is wrong"):
        super().__init__(message)  


class TransferAmount(BaseException):
    def __init__(self, message="you can't transfer negative amounts"):
        super().__init__(message)


class MovieAgeLimitation(BaseException):
    def __init__(self, message="This Movie is not proper for your age group."):
        super().__init__(message)
    

class NoCapacity(BaseException):
    def __init__(self, message="Sorry! All tickets are sold."):
        super().__init__(message)
    

class ScreenTimePassed(BaseException):
    def __init__(self, message="This ticket's screening Time has passed"):
        super().__init__(message)
    

class PasswordLengthError(BaseException):
    def __init__(self, message="Enter at least four characters for password"):
        super().__init__(message)
    

class DuplicateUsernameError(BaseException):
    def __init__(self, message="This username already exists. try again"):
        super().__init__(message)
    
    
class MismatchOfPasswordsError(BaseException):
    def __init__(self, message="new password and repeated new password is not equal toghether"):
        super().__init__(message)
    

class InvalidPasswordError(BaseException):
    def __init__(self, message="Invalid password. try again..."):
        super().__init__(message)
    

class AccessError(BaseException):
    def __init__(self, message="Access to this section is not allowed"):
        super().__init__(message)
    

class InvalidUsernameError(BaseException):
    def __init__(self, message="The username is not exsist. try again"):
        super().__init__(message)
      

class BirthdateInputFormatError(BaseException):
    def __init__(self, message="The input format for birthday is wrong. Please try in the format dd/mm/yyyy."):
        super().__init__(message)    


class WalletError(BaseException):
    def __init__(self, message="Charge the wallet"):
        super().__init__(message) 

    