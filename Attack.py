import random
import os
import textwrap
from blessed import Terminal
from Monsters import *
from Player import *
from Dice import *

term = Terminal()

enemy_list = ['Goblin', 'Orc','Snotling','Witch', 'Zombie','Kobold','Hobgoblin']
#enemy_list = ['Witch']


roll = Dice()

class Attack:
    def __init__(self):
        #self.enemy_instance = globals()[random.choice(enemy_list)]()
        self.enemy_instance = Monsters(random.choice(enemy_list))
        self.player = Player()
    def attackloop(self):
        print(f"You encounter {term.orange}{self.enemy_instance.type}!!{term.normal}")
        loop = 1
        while loop == 1:
            print(f'{term.red}1.Attack {term.normal}| {term.blue}2.Spell {term.normal}| {term.green}3.Enemy Stats {term.normal}| {term.yellow}4.Flee {term.normal}| ')
            inp = input(f"{term.orangered}|>>{term.normal}")
            os.system("cls")
            if(inp == '1'):
                if self.player.HP > 0 and self.enemy_instance.HP > 0:
                    if(self.player.DEX >= self.enemy_instance.DEX):
                        loop = self.player_attack()
                        if loop == 1:
                            if(self.enemy_instance.INT > self.enemy_instance.STR and self.enemy_instance.MP != 0):
                                loop = self.enemy_magic_attack()
                            else:
                                loop = self.enemy_attack()
                    else:
                        if (self.enemy_instance.INT > self.enemy_instance.STR and self.enemy_instance.MP != 0):
                            loop = self.enemy_magic_attack()
                        else:
                            loop = self.enemy_attack()
                        if loop == 1:
                            loop = self.player_attack()
                elif(self.player.HP < 0):
                    print("Game Over")
                    sys.exit()
                else:
                    break
            elif(inp == '2'):
                print(f"1.Zap(MP Cost:2) | 2.Blast(MP Cost:5) | 3.Back | Your MP: {self.player.MP} ")
                mag_inp = input(f'{term.aqua}||>>{term.normal}')
                if(mag_inp == '1'):
                    os.system("cls")
                    if self.player.HP > 0 and self.enemy_instance.HP > 0:
                        if (self.player.DEX >= self.enemy_instance.DEX):
                            if(self.player.MP >= 2):
                                loop = self.player_magic_attack('zap')
                            else:
                                print("You dont have Enought MP")
                            if loop == 1:
                                if (self.enemy_instance.INT > self.enemy_instance.STR and self.enemy_instance.MP >= 2):
                                    loop = self.enemy_magic_attack()
                                else:
                                    loop = self.enemy_attack()
                        else:
                            if (self.enemy_instance.INT > self.enemy_instance.STR and self.enemy_instance.MP >= 2):
                                loop = self.enemy_magic_attack()
                            else:
                                loop = self.enemy_attack()
                            if loop == 1:
                                loop = self.player_attack()
                    elif (self.player.HP < 0):
                        print("Game Over")
                        sys.exit()
                    else:
                        break
                elif(mag_inp == '2'):
                    os.system("cls")
                    if self.player.HP > 0 and self.enemy_instance.HP > 0 and self.player.MP >= 5:
                        if (self.player.DEX >= self.enemy_instance.DEX):
                            if(self.player.MP >= 5):
                                loop = self.player_magic_attack('blast')
                            else:
                                print("You dont have Enought MP")
                            if loop == 1:
                                if (self.enemy_instance.INT > self.enemy_instance.STR and self.enemy_instance.MP != 0):
                                    loop = self.enemy_magic_attack()
                                else:
                                    loop = self.enemy_attack()
                        else:
                            if (self.enemy_instance.INT > self.enemy_instance.STR and self.enemy_instance.MP != 0):
                                loop = self.enemy_magic_attack()
                            else:
                                loop = self.enemy_attack()
                            if loop == 1:
                                loop = self.player_attack()
                    elif (self.player.HP < 0):
                        print("Game Over")
                        sys.exit()
                    elif(self.player.MP < 5):
                        print("You Dont have enought MP")
                    else:
                        break
                elif(mag_inp == '3'):
                    pass
                else:
                    print("¯\_(ツ)_/¯")
            elif(inp == '3'):
                print("---------+-------+----------------------------------------------")
                print(f"Name:{self.enemy_instance.type} | HP:{self.enemy_instance.HP} | MP:{self.enemy_instance.MP} | STR:{self.enemy_instance.STR} | INT:{self.enemy_instance.INT} | DEX:{self.enemy_instance.DEX} | DEF:{self.enemy_instance.DEF} |")
                print("---------+-------+----------------------------------------------")
                self.desc = str(self.enemy_instance.description)
                self.tr = textwrap.wrap(self.desc)
                for self.line in self.tr:
                    print(f"{self.line}")
                print("------------------------------------------------------------------------")
            elif(inp == '4'):
                os.system("cls")
                if(self.player.LUCK > self.enemy_instance.LUCK):
                    print("You Got Away Safely !!")
                    break
                elif(self.player.LUCK == self.enemy_instance.LUCK):
                    ram_value = random.randint(0,1)
                    if(ram_value == 0):
                        print("You tired to Flee but failed")
                        self.enemy_attack()
                    else:
                        print("You Got Away Safely !!")
                        break
                else:
                    print("You tired to Flee but failed")
                    self.enemy_attack()
            else:
                print("¯\_(ツ)_/¯")

    def player_attack(self):
        curr_attack_val = (roll.Roll_attack(self.player.STR,self.enemy_instance.DEF))
        DMG = self.enemy_instance.HP-curr_attack_val

        print("---------------------------------------------------------")
        print(f"You Attacked {term.orange}{self.enemy_instance.type}{term.normal} for {term.red}{curr_attack_val}{term.normal} | {self.enemy_instance.type} HP: {term.orange}{DMG if DMG>=0 else 0}{term.normal}")
        print("---------------------------------------------------------")
        self.enemy_instance.HP -= curr_attack_val
        if(self.enemy_instance.HP <= 0):
            print("---------------------------------------------------------")
            print(f"Enemy {self.enemy_instance.type} Defeated !!!")
            self.player.XP += self.enemy_instance.XP_AWARDED
            self.player.GOLD += self.enemy_instance.GOLD_AWARDED
            print(f"You recived {self.player.XP} XP and {self.player.GOLD} Gold")
            print("---------------------------------------------------------")
            return 0
        else:
            return 1

    def enemy_attack(self):
        curr_attack_val = (roll.Roll_attack(self.enemy_instance.STR,self.player.DEF))
        DMG = self.player.HP-curr_attack_val
        print("---------------------------------------------------------")
        print(f"The {term.orange}{self.enemy_instance.type}{term.normal} attacked {term.green}{self.player.name}{term.normal} for {term.red}{curr_attack_val}{term.normal} | {self.player.name} HP: {term.green}{DMG if DMG>=0 else 0}{term.normal} ")
        print("---------------------------------------------------------")
        self.player.HP -= curr_attack_val
        if(self.player.HP <= 0):
            print("Game Over")
            sys.exit()
        else:
            return 1

    def player_magic_attack(self,type):
        self.type = type
        if (self.type == 'blast'):
            curr_attack_val = (roll.Roll_magic(self.player.INT, self.enemy_instance.DEF,self.type,5))
        elif (self.type == 'zap'):
            curr_attack_val = (roll.Roll_magic(self.player.INT, self.enemy_instance.DEF,self.type,2))
        else:
            print("Error code #1")
        DMG = self.enemy_instance.HP - curr_attack_val
        if(type == 'blast'):
            self.player.MP -= 5
        else:
            self.player.MP -= 2
        print("---------------------------------------------------------")
        print(f"You Attacked {term.orange}{self.enemy_instance.type}{term.normal} for {term.blue}{curr_attack_val}{term.normal} | {self.enemy_instance.type} HP: {term.orange}{DMG if DMG >= 0 else 0}{term.normal} | {term.green}{self.player.name}{term.normal} MP: {term.blue}{self.player.MP}{term.normal}")
        print("---------------------------------------------------------")
        self.enemy_instance.HP -= curr_attack_val
        if (self.enemy_instance.HP <= 0):
            print("---------------------------------------------------------")
            print(f"Enemy {self.enemy_instance.type} Defeated !!!")
            self.player.XP += self.enemy_instance.XP_AWARDED
            self.player.GOLD += self.enemy_instance.GOLD_AWARDED
            print(f"You recived {self.enemy_instance.XP_AWARDED} XP and {self.enemy_instance.GOLD_AWARDED} Gold")
            print("---------------------------------------------------------")
            return 0
        else:
            return 1

    def enemy_magic_attack(self):
        curr_attack_val = (roll.Roll_magic(self.enemy_instance.INT, self.player.DEF,'',5))
        DMG = self.player.HP - curr_attack_val
        print("---------------------------------------------------------")
        print(
            f"The {term.orange}{self.enemy_instance.type}{term.normal} attacked {term.green}{self.player.name}{term.normal} for {term.red}{curr_attack_val}{term.normal} | {self.player.name} HP: {term.green}{DMG if DMG >= 0 else 0}{term.normal} ")
        print("---------------------------------------------------------")
        self.player.HP -= curr_attack_val
        if (self.player.HP <= 0):
            print("Game Over")
            sys.exit()
        else:
            return 1
