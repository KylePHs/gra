
import random
import os
import time
import postacie
from postacie import Mag
from postacie import Archer
from postacie import Warior
from postacie import Furas
import json
from postacie import Postac



def menu():
    os.system('cls')
    print("n - new game\n"
          "d - DLC\n"
          "e - exit")
    start = input("-> ")
    
    if start == "n":
        os.system('cls')
        time.sleep(1)
        print("PHOENIX STUDIO\n"
              "   present:   ")
        time.sleep(2)
        print("Projekt na informatyke")
        os.system('cls')
        create_player()
    
    
    elif start == "d":
        print("Your DLC is under construction\n")
        time.sleep(3)
        menu()
    elif start == "e":
        print("Miłego dnia")
        quit()
        
          

def create_player():
    print("Wpisz imie")
    neme = input("-> ")
    
        
    print("""
          Wybierz klase:
          m - Mag
          a - Archer
          w - Warior
          f - Furry
          """)
    clas = input("-> ")
    if clas == "m":
        c = Mag()
    elif clas == "a":
        c = Archer()
    elif clas == "w":
        c = Warior()
    elif clas == "f":
        c = Furas()
     
    player = Postac(neme,c)    
    Postac.inf()

    
create_player()

        
    
    
          

          
          
          

