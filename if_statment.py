

from pickle import TRUE
from tkinter.tix import Tree


userName = input("Enter user name :")
password = input("Enter password :")

# or / and 
if(len(password) >= 8 or len(userName) >= 6):
    print("Welcome")
# elif:
     #........
else:
    print("Password lengith must be greatin than 7")