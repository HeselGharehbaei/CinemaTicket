import pickle


class Movie:
    movies_list = {}

    def __init__(self, name: str, genere: str, age_limit: int, price: float):
        self.name = name
        self.genere = genere
        self.age_limit = age_limit
        self.price = price
        self.movies_list[self.name] = self
        self.save_data()

    @staticmethod
    def load_movies():
        with open("data/movies.pickle", "rb") as file:
            return pickle.load(file)

    def save_data(self) -> None:
        with open("data/movies.pickle", "ab") as file:
            pickle.dump(self.movies_list, file)
            self.movies_list.clear()

    @classmethod
    def get_movie(cls, name: str) -> object:
        movies = cls.load_movies()
        return movies[name]

    def __str__(self) -> str:
        return f"{self.name}:\nGenre: {self.genere}\tAgelimit: +{self.age_limit}\tPrice: {self.price}"
