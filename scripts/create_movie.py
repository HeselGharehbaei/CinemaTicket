import os, sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)


from argparse import ArgumentParser
from movie import Movie


def main():
    parser = ArgumentParser(
        description="This script is for creating Movie object by admins."
    )
    parser.add_argument("--name", type=str, help="Movie Name", required=True)
    parser.add_argument("--genere", type=str, help="Movie genere", required=True)
    parser.add_argument("--age_limit", type=int, help="Movie age limit", required=True)
    parser.add_argument("--price", type=float, help="Movie price", required=True)

    args = parser.parse_args()
    Movie(args.name, args.genere, args.age_limit, args.price)


if __name__ == "__main__":
    main()
