import sys
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)


from user import User


manager_1= User.sign_up("Hesel", "1234", "30/07/1370", "09910902715", "MANAGER")
manager_2= User.sign_up("Mahsa", "1234", "25/05/1378", "09384625861", "MANAGER")