
from getpass import getpass
from random import choice

p_win = [("paper","stone"),("stone","scissor"),("scissor","paper")]  #these conditions are for winning of player1
p = getpass("\n Player  : ").strip().lower()
choices = ['stone','paper','scissor']
comp = choice(choices)
if p in choices:
        if (p,comp) in p_win:
            print(f"\n PLAYER won......with choices \n Player --> {p.upper()} and Computer --> {comp.upper()}")
        elif p == comp:
            print("\n TIE.....")
        else:
            print(f"\n COMPUTER won......with choices \n Player -->{p.upper()} and Computer --> {comp.upper()}")
else:
    print("\n Incorrect choice by PLAYER")
