from abc import ABC, abstractmethod
from utils.exceptions import MinBalanceError


class Bank(ABC):
    MIN_BALANCE = 10_000

    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance: float) -> float:
        if self._balance < self.MIN_BALANCE:
            raise MinBalanceError("balance can't be below 10000 tomans")
        self._balance = balance

    def __add__(self, amount: float) -> None:
        self._balance += amount

    def __sub__(self, amount: float) -> None:
        self._balance -= amount

    @abstractmethod
    def transfer(self, other: "Bank", amount: float) -> None:
        pass

    @staticmethod
    def to_rial(amount: float) -> float:
        return amount * 10

    def __str__(self) -> str:
        return f"{self.owner}: {self._balance:,} Toman"

    def __repr__(self) -> str:
        dic = vars(self)
        dic["rial"] = self.to_rial(self._balance)
        return str(dic)

    def __eq__(self, other: "Bank") -> bool:
        return self._balance == other._balance
