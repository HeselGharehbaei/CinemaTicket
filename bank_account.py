from bank import Bank
import json
from utils.exceptions import MinBalanceError, PasswordCvv2Error, TransferAmount
from credit_card import generate_credit_card_number
from random import randint


class BankAccount(Bank):
    ــMIN_BALANCE = 10_000
    transaction_fee = 100

    def __init__(
        self,
        owner: str,
        balance: float,
        password: str,
        cvv2: str = None,
        id: str = None,
    ) -> None:
        super().__init__(owner, balance)
        self.password = password
        if id == None:
            self.id = generate_credit_card_number()
        else:
            self.id = id
        if cvv2 == None:
            self.cvv2 = randint(1000, 9999)
        else:
            self.cvv2 = cvv2
        self.save_data()

    def save_data(self) -> None:
        with open("data/bankaccounts.json", "r+") as file:
            existing_data = json.load(file)
            file.seek(0)
            file.truncate()
            existing_data[self.id] = self.__dict__
            json.dump(existing_data, file, indent=2)

    @staticmethod
    def load_data() -> dict:
        with open("data/bankaccounts.json", "r") as file:
            return json.load(file)

    @classmethod
    def get_account(cls, id: str) -> object:
        accounts_data = cls.load_data()
        dict = accounts_data[id]
        dict["balance"] = dict["_balance"]
        del dict["_balance"]
        return cls(**dict)

    def check_infoـvalidation(self, cvv2, password) -> bool:
        account_data = self.get_account(self.id)
        return (
            True
            if account_data.cvv2 == cvv2 and account_data.password == password
            else PasswordCvv2Error
        )

    def __add__(self, amount: float) -> None:
        if amount < 0:
            raise TransferAmount
        if self._balance + amount < self.MIN_BALANCE:
            raise MinBalanceError
        return super().__add__(amount)

    def __sub__(self, amount: float) -> None:
        if amount < 0:
            raise TransferAmount
        if self._balance - amount < self.MIN_BALANCE:
            raise MinBalanceError
        return super().__sub__(amount)

    def transfer(self, other: Bank, amount: float) -> None:
        if amount < 0:
            raise TransferAmount
        self.__sub__(amount + BankAccount.transaction_fee)
        other.__add__(amount)
