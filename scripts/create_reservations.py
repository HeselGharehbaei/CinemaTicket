import os, sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)


from argparse import ArgumentParser
from datetime import datetime
from reservation import Reservation
from cinema import Cinema
from movie import Movie


def main():
    parser = ArgumentParser(
        description="This script is for creating reservation objects by admins."
    )

    parser.add_argument("--movie", help="Name of the movie", required=True, type=str)
    parser.add_argument(
        "--cinema", help="Name of the cinema hosting the movie", required=True, type=str
    )
    parser.add_argument(
        "--salon",
        help="The cinema salon screening the movie",
        required=True,
        type=str,
    )
    parser.add_argument(
        "--screentime", help="screening date and time", required=True, type=lambda s: datetime.strptime(s, '%m/%d/%y %H:%M:%S')
    )

    args = parser.parse_args()

    movie = Movie.get_movie(args.movie)
    cinema = Cinema.get_cinema(args.cinema)

    Reservation(movie, cinema, args.salon, args.screentime)


if __name__ == "__main__":
    main()
