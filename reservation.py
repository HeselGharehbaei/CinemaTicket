import pickle
from cinema import Cinema
from movie import Movie
from user import User
from datetime import datetime
from utils.exceptions import MovieAgeLimitation, NoCapacity, ScreenTimePassed


class Reservation:
    data = {}

    def __init__(self, movie: Movie, cinema: Cinema, salon: str, screen_time: datetime):
        self.movie = movie
        self.cinema = cinema
        self.salon = salon
        self.capacity = self.cinema[salon]
        self.screen_time = screen_time
        self.data[self.movie.name] = self
        self.save_data()

    def save_data(self):
        with open("data/reservation.pickle", "ab") as file:
            pickle.dump(self.data, file)
            self.data.clear()

    @classmethod
    def load(cls):
        try:
            with open("data/reservation.pickle", "rb") as file:
                reservation_data = pickle.load(file)
        except EOFError as err:
            return dict()
        return reservation_data

    def make_reservation(self, user: User):
        if self.capacity == 0:
            raise NoCapacity
        if not self.age_check:
            raise MovieAgeLimitation
        if not self.screentime_check:
            raise ScreenTimePassed
        # check with user:
        try:
            user.buy_movie(self.movie,self.final_price(user))
            self.capacity -= 1
        except:
            return "reservation failed"

    def age_check(self, user: User):
        age = datetime.now().date() - user.birthday
        age_years = int(age.days / 365)
        if self.movie.age_limit < age_years:
            return True

    def screentime_check(self):
        if self.screen_time > datetime.now():
            return True

    @staticmethod
    def apply_discount(user: User) -> float:
        since_joined = datetime.now().date() - user.join_date
        days_joined = int(since_joined.days)
        coeff = 1 - (days_joined / 100)
        if user.subscription == "Gold":
            coeff *= 0.5
        elif user.subscription == "Silver":
            coeff *= 0.8
        return coeff

    def final_price(self, user: User):
        price = self.apply_discount(user) * self.movie.price
        if (
            user.birthday.day == datetime.now().day
            and user.birthday.month == datetime.now().month
        ):
            price *= 0.5
        return price
