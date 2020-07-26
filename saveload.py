import json
from Player import *
from inventory_player import *

pinv = P_inv()
player = Player()

class SaveLoad:
    def savegame(self,name,HP,MP,STR,INT,DEX,DEF,LUCK,XP,GOLD,max_HP,max_MP,eq_wep,eq_arm,lvl):
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
        self.max_HP = max_HP
        self.max_MP = max_MP
        self.eq_wep = eq_wep
        self.eq_arm = eq_arm
        self.level = lvl

        print(f"\nSaving: -> Name:{self.name} | HP:{self.HP} | MP:{self.MP} | STR:{self.STR} | INT:{self.INT} | DEX:{self.DEX} | DEF:{self.DEF} | LUCK:{self.LUCK} | XP:{self.XP} | GOLD:{self.GOLD} | 'Level:{self.level}'\n")

        self.password = str(input("Enter Password (You will be asked to 'Enter Password While Loading' your save!): \n"))
        self.ps_lst = []
        for i in self.password:
            self.ps_lst.append(ord(i))
        self.str1 = "".join(str (e) for e in self.ps_lst)
        self.savedict = {}
        self.savedict['player'] = []
        self.savedict['player'].append({"name": self.name ,"HP": self.HP ,"MP": self.MP ,"STR": self.STR ,"INT": self.INT ,"DEX": self.DEX ,"DEF": self.DEF, "LUCK": self.LUCK, "XP" : self.XP, "GOLD": self.GOLD,"MAX_HP" : self.max_HP ,"MAX_MP" : self.max_MP, "password": self.str1, "eq_wep" : self.eq_wep, "eq_arm" : self.eq_arm, "weapons" : pinv.inv['weapons'], "armours" : pinv.inv['armours'], "potions" : pinv.inv['potions'], "level" : self.level })

        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(self.savedict, f, ensure_ascii=False)
        print("Save Sucessful !!")

    def loadgame(self):
        with open('data.json', 'r', encoding='utf-8') as f:
            self.game_data = json.loads(f.read())

        password = self.game_data['player'][0]['password']
        print(f"Loading Player {self.game_data['player'][0]['name']}'s data\n")
        self.pass_inp = input("Enter your password\n")
        self.ps_lst = []
        for i in self.pass_inp:
            self.ps_lst.append(ord(i))
        self.str1 = "".join(str(e) for e in self.ps_lst)
        if self.str1 == password:
            player.load_val(self.game_data['player'][0]['name'],self.game_data['player'][0]['HP'],self.game_data['player'][0]['MP'],self.game_data['player'][0]['STR'],self.game_data['player'][0]['INT'],self.game_data['player'][0]['DEX'],self.game_data['player'][0]['DEF'],self.game_data['player'][0]['LUCK'],self.game_data['player'][0]['XP'],self.game_data['player'][0]['GOLD'], self.game_data['player'][0]['max_HP'],self.game_data['player'][0]['max_MP'],self.game_data['player'][0]['eq_wep'],self.game_data['player'][0]['eq_arm'],self.game_data['player'][0]['level'])
            pinv.inv['weapons'] = self.game_data['player'][0]['weapons']
            pinv.inv['armours'] = self.game_data['player'][0]['armours']
            pinv.inv['potions'] = self.game_data['player'][0]['potions']
            return  0
        else:
            return 1
