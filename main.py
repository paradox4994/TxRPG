import os
import sys
import random
import blessed
from Player import *
from Monsters import *
from Attack import *
from debug import *
from saveload import *
from inventory_player import *
from shop import *


player = Player()
sv = SaveLoad()
pinv = P_inv()


term = blessed.Terminal()

class mainScreen():
    def mainLoop(self):
        while True:
            os.system('cls')
            print("1.Play\n2.Load\n3.Exit")
            ip = input(">>")
            if(ip== '1'):
                player_start = playerStart()
                player_start.char_selection()
                break
            if(ip== '2'):
                flag = sv.loadgame()
                if flag == 0:
                    break
                else:
                    print("Wrong Password\n")
            if(ip== '3'):
                print("Bye!")
                sys.exit()
            else:
                print("Enter Valid Options")
        os.system('cls')
        print("Type !help for list of commands")
        while True:
            cmd = input(">>")
            os.system('cls')
            if(cmd == "!stats"):                                            #stats
                player.status()
            elif(cmd == "!help"):                                           #Help
                os.system('cls')
                print("!explore, !stats, !inv !quit !save !location !equipment !use !uprade !shop")
            elif(cmd == "!quit"):                                           #Quit
                os.system('cls')
                qans = input("Quit Game : [Y/N] ?")
                if(qans == 'Y' or qans == "y"):
                    sys.exit()
                else:
                    pass
            elif (cmd == "!inv"):                                           #Inventory
                os.system('cls')
                print("1.List 2.Equip 3.Unequip 4.Back")
                while True:
                    ii = input(f"{term.limegreen}<>{term.normal}")
                    if ii == '1':
                        pinv.inv_list()
                    elif ii == '2':
                        pinv.equip()
                    elif ii == '3':
                        print("1.Weapon 2.Armour 3.Back")
                        pinv.unequip(input("<<>"))
                    elif ii == '4':
                        break
                    else:
                        print("Enter Valid Option!")
            elif (cmd == "!explore"):                                       #Explore
                os.system('cls')
                os.system("cls")
                atk = Attack()
                atk.attackloop()
                del atk
            elif (cmd == "!save"):                                          #Save
                os.system('cls')
                sv.savegame(player.name,player.HP,player.MP,player.STR,player.INT,player.DEX,player.DEF,player.LUCK,player.XP,player.GOLD,player.MAX_HP,player.MAX_MP,player.eq_wep,player.eq_arm,)
            elif (cmd == "!location"):                                      #Location
                os.system('cls')
                pass
            elif (cmd == "!debug"):                                         #Debug
                os.system('cls')
                Debug.debug(self)
            elif (cmd == '!equipment'):                                     #Equipment
                os.system('cls')
                player.equipments()
                input("Press Enter To go back")
            elif (cmd == '!use'):                                     #Equipment
                os.system('cls')
                pinv.use_potion()
            elif (cmd == '!upgrade'):                                     #Equipment
                os.system('cls')
                pass
            elif (cmd == '!shop'):                                     #Equipment
                os.system('cls')
                shop = Shop()
            else:
                print("Type !help for more info")

        #atk = Attack()
        #atk.battle()



if __name__ == "__main__":
    game = mainScreen()
    game.mainLoop()
