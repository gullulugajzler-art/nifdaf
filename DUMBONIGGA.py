import os
import sys
import time 
import subprocess
import colorama
import keyboard
from keyboard import press
from colorama import Fore, Style
from time import sleep


ratter = "DUMBO RAT"

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    
def main():    
     
    print(Fore.RED + f"The ratter is {ratter}!" + Style.RESET_ALL)
    print(Fore.GREEN + f"The ratter is {ratter}!" + Style.RESET_ALL)
    print(Fore.BLUE + f"The ratter is {ratter}!" + Style.RESET_ALL)
    print(Fore.MAGENTA + f"The ratter is {ratter}!" + Style.RESET_ALL)
    print(Fore.CYAN + f"The ratter is {ratter}!" + Style.RESET_ALL)
    print(Fore.WHITE + f"The ratter is {ratter}!" + Style.RESET_ALL)
    print(Fore.YELLOW + f"The ratter is {ratter}!" + Style.RESET_ALL)
    sleep(0.1)
    os.system(r"start C:\Users\%USERNAME%\Desktop\DUMBONIGGA.py")
    return main()


if __name__ == "__main__":
    main()