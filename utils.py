from os import system, name
from time import sleep

def clear(time = 2):
    sleep(time)
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def handleError(error):
    print(error)
    print(f'Something goes wrong try again')
    
