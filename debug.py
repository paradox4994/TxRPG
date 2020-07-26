from Player import *
from Monsters import *
from Attack import *
from inventory_player import *

pinv = P_inv()

class Debug:
    def debug(self):
        while True:
            inp = input('<|>')
            if(inp == 'pdmg'):
                player.HP -= 1
                print(player.HP)
            elif (inp == 'pinc'):
                player.HP += 1
                print(player.HP)
            elif(inp == 'pkill'):
                player.HP = 0
                print(player.HP)
            elif(inp == 'edmg'):
                enemy_instance.HP -= 1
                print(enemy_instance.HP)
            elif (inp == 'einc'):
                enemy_instance.HP += 1
                print(enemy_instance.HP)
            elif(inp == 'ekill'):
                enemy_instance.HP = 0
                print(enemy_instance.HP)
            elif(inp == 'addgold' ):
                player.GOLD += 10
                print(player.GOLD)
            elif(inp == 'addxp'):
                player.XP += 10
                print(player.XP)
            elif(inp == 'maxl'):
                player.LUCK = 12
                print(player.LUCK)
            elif(inp == 'addpot1'):
                pinv.add_pot('Healing Potion')
            elif (inp == 'addpot2'):
                pinv.add_pot('Mana Potion')
            elif (inp == 'addwep1'):
                pinv.add_wep('Simple Sword')
            elif (inp == 'remwep1'):
                pinv.rem_wep('Simple Sword')
            elif (inp == 'addarm1'):
                pinv.add_arm('Leather Armour')
            elif (inp == 'remarm1'):
                pinv.rem_arm('Leather Armour')
            else:
                break

