from bank import Bank
import json
from utils.exceptions import MinBalanceError, PasswordCvv2Error, TransferAmount


class BankAccount(Bank):
    ــMIN_BALANCE = 10_000
    transaction_fee = 100

    def __init__(self, owner: str, balance: float, cvv2: str, password: str) -> None:
        super().__init__(owner, balance)
        self.cvv2 = cvv2
        self.password = password
        self.save_data()

    def save_data(self) -> None:
        with open("data/bankaccounts.json","r+") as file:
            existing_data = json.load(file)
            file.seek(0)
            file.truncate()
            existing_data[self.owner] = self.__dict__
            json.dump(existing_data, file, indent=2)

    @staticmethod
    def load_data() -> dict:
        with open("data/bankaccounts.json", "r") as file:
            return json.load(file)

    @classmethod
    def get_account(cls,owner):
        accounts_data = cls.load_data()
        dict = accounts_data[owner]
        dict["balance"] = dict["_balance"]
        del dict["_balance"]
        return cls(**dict)

    def check_infoـvalidation(self) -> bool:
        account_data = self.get_account(self.owner)
        return (
            True
            if account_data.cvv2 == self.cvv2
            and account_data.password == self.password
            else False
        )

    def __add__(self, amount: float) -> None:
        if not self.check_infoـvalidation():
            raise PasswordCvv2Error("Password or CVV2 is wrong")
        if self._balance + amount < self.MIN_BALANCE:
            raise MinBalanceError("balance can't be below 10000 tomans")
        return super().__add__(amount)

    def __sub__(self, amount: float) -> None:
        if not self.check_infoـvalidation():
            raise PasswordCvv2Error("Password or CVV2 is wrong")
        if self._balance - amount < self.MIN_BALANCE:
            raise MinBalanceError("balance can't be below 10000 tomans")
        return super().__sub__(amount)

    def transfer(self, other: Bank, amount: float) -> None:
        if amount < 0:
            raise TransferAmount("you can't transfer negative amounts")
        self.__sub__(amount + BankAccount.transaction_fee)
        other.__add__(amount)
