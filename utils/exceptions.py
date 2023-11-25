

class MinBalanceError(Exception):
    print("balance can't be below 10000 tomans")

class PasswordCvv2Error(Exception):
    print("Password or CVV2 is wrong")

class TransferAmount(Exception):
    print("you can't transfer negative amounts")

class MovieAgeLimitation(Exception):
    print("This Movie is not proper for your age group.")

class NoCapacity(Exception):
    print("Sorry! All tickets are sold.")

class ScreenTimePassed(Exception):
    print("This ticket's screening Time has passed")