# import only system from os 
from os import system, name 
import sys
# import sleep to show output for some time period 
from time import sleep 
from platform import system
# if system() == 'Windows':
#     from msvcrt import getch
from getkey import getkey, keys

def run_menu():

    s = ("************MAIN MENU**************")
    menu= { "1": "msds compound",
            "2": "only ingredients compound", 
            "q": "Quit/Log Out"
    }
    for k, v in menu.items():
        s = s + '\n' + '\t {k} : {v}'.format(k=k,v=v)
    s = s + '\nPlease enter your choice: '

    choice = input(s)
    if choice in menu:
        return(choice)
    elif choice=="Q" or choice=="q" or choice=="й" or choice=="Й":
        sys.exit
    else:
        print("You must only select either 1 or 2")
        print("Please try again")
        run_menu()



# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 