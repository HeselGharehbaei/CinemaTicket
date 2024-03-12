import os, sys,json
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)


from argparse import ArgumentParser
from cinema import Cinema


def main():
    parser = ArgumentParser(
        description="This script is for creating Cinema object by admins."
    )
    parser.add_argument("--name", type=str, help="Name of the cinema", required=True)
    parser.add_argument(
        "--salon_count", type=int, help="Number of salons in the cinema", required=True
    )
    parser.add_argument(
        "--salons", type=json.loads, help="Dictionary representing salons", required=True
    )

    args = parser.parse_args()
    Cinema(args.name, args.salon_count, args.salons)


if __name__ == "__main__":
    main()
