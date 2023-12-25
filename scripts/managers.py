import sys
import os
from argparse import ArgumentParser


current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)


from user import User, UserType


parser= ArgumentParser(description= "Manager User")
parser.add_argument("username", metavar="USERNAME", type=str, help='your username not be doplicated')
parser.add_argument("password", metavar="PASSWORD", type=str, help='your password with 4 or upper than 4 character')
parser.add_argument("birthday", metavar="BIRTHDAY", type=str, help='your birthday in format of dd/mm/yyyy')
parser.add_argument("-ph", "--phonenumber", metavar="PHONE NUMBER", type=str, help='your phone number')
parser.add_argument("-ut", "--user_type", metavar="USER TYPE", type= object, help='your user type that manager or normal user')
args = parser.parse_args()

manager= User(args.username, args.password, args.birthday, args.phonenumber, user_type= UserType.MANAGER)