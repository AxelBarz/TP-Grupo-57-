import os 
from colorama import *

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def pedir_dato(mensaje): 
    dato=input(mensaje)
    while dato.strip() == "":
        dato=input(Fore.LIGHTRED_EX+"Por favor escribe el dato correspondiente: ")
    return dato