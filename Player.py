import os
import sys
import random
import xml.etree.ElementTree as ET
from time import sleep
from blessed import Terminal

term = Terminal()

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Player(metaclass=Singleton):
    def set_val(self,name,HP,MP,STR,INT,DEX,DEF):
        self.inp = '1'

        mytree = ET.parse('entities.xml')
        myroot = mytree.getroot()

        self.name = name
        self.HP = HP
        self.MP = MP
        self.STR = STR
        self.INT = INT
        self.DEX = DEX
        self.DEF = DEF
        self.LUCK = random.randint(5, 12)
        self.XP = 0
        self.GOLD = 0
        self.LEVEL = 0
        self.MAX_HP = HP
        self.MAX_MP = MP
        self.all_players = myroot.findall('player')
        for p in self.all_players:
            if p.find('type').text == self.inp:
                self.eq_wep = p.find('eq_wep').text
                self.eq_arm = p.find('eq_arm').text

    def status(self):
        print(f"Name:{self.name} | HP:{term.red}{self.HP}{term.normal}/{self.MAX_HP} | MP:{term.blue}{self.MP}{term.normal}/{self.MAX_MP} | STR:{self.STR} | INT:{self.INT} | DEX:{self.DEX} | DEF:{self.DEF} | LUCK:{self.LUCK} | XP:{self.XP} | GOLD:{self.GOLD} | Level:{self.LEVEL}")

    def equipments(self):
        print(f'Equipped Weapon : {self.eq_wep}')
        print(f'Equipped Armour : {self.eq_arm}')

    def load_val(self,name,HP,MP,STR,INT,DEX,DEF,LUCK,XP,GOLD,max_HP,max_MP,eq_wep,eq_arm,lvl):
        self.name = name
        self.HP = HP
        self.MP = MP
        self.STR = STR
        self.INT = INT
        self.DEX = DEX
        self.DEF = DEF
        self.LUCK = LUCK
        self.XP = XP
        self.GOLD = GOLD
        self.MAX_HP = max_HP
        self.MAX_MP = max_MP
        self.eq_wep = eq_wep
        self.eq_arm = eq_arm
        self.LEVEL = lvl


class playerStart():

    def dis(self,i):
        if i < 4:
            print(f'HP: {self.HP}')
            print(f'MP: {self.MP}')
            print(f'STR: {self.STR}')
            print(f'INT: {self.INT}')
            print(f'DEX: {self.DEX}')
            print(f'DEF: {self.DEF}')
            sleep(0.2)
            os.system('cls')
        else:
            print(f'HP: {self.HP}')
            print(f'MP: {self.MP}')
            print(f'STR: {self.STR}')
            print(f'INT: {self.INT}')
            print(f'DEX: {self.DEX}')
            print(f'DEF: {self.DEF}')




    def charroll(self):
        for i in range(5):
            print('\n')
            self.HP = random.randint(60,100)
            if self.HP > 75:
                self.MP = random.randint(60,80)
            else:
                self.MP = random.randint(40,60)
            self.STR = random.randint(15,25)
            if self.STR > 20:
                self.INT = random.randint(15,25)
            else:
                self.INT = random.randint(23,30)
            self.DEX = random.randint(0,15)
            self.DEF = random.randint(1,3)
            playerStart.dis(self,i)

    def char_selection(self):
        os.system('cls')
        lp = 1
        self.cnt = 3
        self.name = input("Enter Your Name\n")
        playerStart.charroll(self)
        while(lp == 1):
            if self.cnt > 0:
                inp = input(f"\n1.Accept \t 2. Roll Again ({self.cnt})\n")
                if(inp == '1'):
                    player = Player()
                    player.set_val(self.name,self.HP,self.MP,self.STR,self.INT,self.DEX,self.DEF)
                    lp = 0
                elif(inp == '2'):
                    self.cnt -= 1
                    os.system('cls')
                    playerStart.charroll(self)
                else:
                    print("Please enter valid input\n")
            else:
                player = Player()
                player.set_val(self.name,self.HP,self.MP,self.STR,self.INT,self.DEX,self.DEF)
                input('\npress any key to continue..')
                lp = 0