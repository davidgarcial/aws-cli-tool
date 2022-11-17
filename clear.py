from os import system, name
from time import sleep
 
def clear(time = 0.5):
    sleep(time)
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
