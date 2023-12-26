import pickle


class Cinema:
    cinemas_list = {}

    def __init__(self, name: str, salon_count: int, salons: dict):
        self.name = name
        self.salon_count = salon_count
        self.salons = salons
        self.cinemas_list[self.name] = self
        self.save_data()

    @staticmethod
    def load_cinemas():
        with open("data/cinemas.pickle", "rb") as file:
            return pickle.load(file)

    def save_data(self) -> None:
        with open("data/cinemas.pickle", "ab") as file:
            pickle.dump(self.cinemas_list, file)
            self.cinemas_list.clear()

    @classmethod
    def get_cinema(cls, name: str) -> object:
        cinemas = cls.load_cinemas()
        return cinemas[name]
    
    def __str__(self) -> str:
        return f"Cinema {self.name}:\nSalons:{self.salons}"
    

