from Player import *
from inventory_player import *
from Dice import *
from blessed import Terminal

import xml.etree.ElementTree as ET
import textwrap
import os

term = Terminal()

class Shop:
    def __init__(self):
        print("Welcome to the shop Adventrer\n")
        while(True):
            print(f"Use {term.goldenrod1}!buy{term.normal} {term.turquoise1}!sell {term.normal} {term.pink}!luckroll{term.normal} or !back to return")
            print(f"You have {player.GOLD} Gold")
            ii = input(f"{term.goldenrod1}=>{term.normal}")
            if ii == '!buy':
                Shop.buy(self)
            elif ii == '!sell':
                Shop.sell(self)
            elif ii == '!luckroll':
                Shop.luckroll(self)
            elif ii == '!back':
                break
            else:
                print('Invalid Choice')
            os.system('cls')

    def load(self):
        pass

    def buy(self):
        pass

    def sell(self):
        pass
    def luckroll(self):
        print("Enter gold to roll")
        gi = int(input(f'{term.goldenrod1}=>{term.normal} <->'))
        if gi > player.GOLD:
            print(f'{term.goldenrod1}=>{term.normal} <-> You cant add Gold more then you own')
            input()
        else:
            print("Enter any number between 1 to 12")
            lnum = int(input(f'{term.goldenrod1}=>{term.normal} <->'))
            self.temp = random.randint(1,12)
            if lnum == self.temp:
                print(f'{term.goldenrod1}=>{term.normal} <-> You Won, your roll is doubled')
                input()
                player.GOLD = player.GOLD+(2*gi)
            else:
                print(f'{term.goldenrod1}=>{term.normal} <-> You Loose, better luck next time')
                print(f'{term.goldenrod1}=>{term.normal} <-> Your No:{lnum} | Rolled No:{self.temp}')
                player.GOLD = player.GOLD - gi
                input()
