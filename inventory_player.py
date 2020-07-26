import xml.etree.ElementTree as ET
from blessed import Terminal
from Player import *

term = Terminal()
player = Player()


mytree = ET.parse('items.xml')
myroot = mytree.getroot()

mytreepl = ET.parse('entities.xml')
myrootpl = mytreepl.getroot()

#print(findspitem('potion','name','Healing Potion'))

def finditem(item,attrib,iname):
        items = myroot.findall(f'./{item}')
        for i in items:
            if i.find(f'.//{attrib}').text == iname:
                return i.find(f'.//{attrib}').text

def findlist(self,item,type):
        items = myrootpl.findall(f'./{item}')
        mylist = []
        for i in items:
            mylist.append(i.attrib['type'])
        return mylist




class P_inv(metaclass=Singleton):
    def __init__(self):
        self.w_list = []
        self.a_list = []
        self.p_list = []
        self.hp_count = 0
        self.mp_count = 0
        self.inv = {'weapons':  self.w_list , 'armours' : self.a_list , 'potions' :  self.p_list }

    def inv_add(self,name):
        pass


    def inv_pop(self):
        pass

    def inv_list(self):
        self.newwlist = list(dict.fromkeys(self.inv["weapons"]))
        self.newalist = list(dict.fromkeys(self.inv["armours"]))
        self.newplist = list(dict.fromkeys(self.inv["potions"]))
        for self.w in self.newwlist:
            print(f'{term.red}Weapon{term.normal} : {self.w} : {self.inv["weapons"].count(self.w)} ')
        for self.w in self.newalist:
            print(f'{term.yellow}Armour{term.normal} : {self.w} : {self.inv["armours"].count(self.w)} ')
        for self.w in self.newplist:
            print(f'{term.blue}Potion{term.normal} : {self.w} : {self.inv["potions"].count(self.w)} ')

    def potions(self):
        pass

    def equip(self):
        print("1.Weapon 2.Armour 3.Back")
        while True:
            ip = input("<>>")
            if ip == '1':
                self.newwlist = list(dict.fromkeys(self.inv["weapons"]))
                for self.w in self.newwlist:
                    print(f'{term.red}Weapon{term.normal} : {self.w} : {self.inv["weapons"].count(self.w)}')
                ii = str(input("Enter  exact name of Weapon to equip >> "))
                self.equip_weapon(ii)
            elif ip == '2':
                self.newalist = list(dict.fromkeys(self.inv["armours"]))
                for self.w in self.newalist:
                    print(f'{term.yellow}Armour{term.normal} : {self.w} : {self.inv["armours"].count(self.w)} ')
                ii = str(input("Enter  exact name of Armour to equip >> "))
                self.equip_armour(ii)
            elif ip == '3':
                break
            else:
                print("Enter Valid Option!")


    def unequip(self,num):
        self.num = num
        if self.num == '1':
            if player.eq_wep == 'None':
                print("Nothing Equiped")
            else:
                self.curr_item = player.eq_wep
                player.eq_wep = 'None'
                self.add_wep(self.curr_item)
                print(f"{self.curr_item} unequipped")
        elif self.num == "2":
            if player.eq_arm == 'None':
                print("Nothing Equiped")
            else:
                self.curr_item = player.eq_arm
                player.eq_arm = 'None'
                self.add_arm(self.curr_item)
                print(f"{self.curr_item} unequipped")
        else:
            print("")


    def add_wep(self,name):
        self.name = name
        self.inv['weapons'].append(self.name)
    def rem_wep(self,name):
        self.name = name
        self.inv['weapons'].remove(self.name)
    def add_arm(self,name):
        self.name = name
        self.inv['armours'].append(self.name)
    def rem_arm(self,name):
        self.name = name
        self.inv['armours'].remove(self.name)
    def add_pot(self,name):
        self.name = name
        self.inv['potions'].append(self.name)
    def rem_pot(self,name):
        self.name = name
        self.inv['potions'].remove(self.name)
    def add_item(self):
        pass
    def rem_team(self):
        pass
    def equip_weapon(self,name):
        self.name = name
        if self.name == player.eq_wep:
            print("You have already equipped this Weapon")
        elif self.name not in self.inv['weapons']:
            print(f"You dont have {self.name} in your inventory")
        else:
            player.eq_wep = self.name
            self.rem_wep(self.name)
            print(f'{term.red}{self.name}{term.normal} equiped')

    def equip_armour(self,name):
        self.name = name
        if self.name == player.eq_arm:
            print("You have already equipped this Armour")
        elif self.name not in self.inv['armours']:
            print(f"You dont have {self.name} in your inventory")
        else:
            player.eq_arm = self.name
            self.rem_arm(self.name)
            print(f'{term.yellow}{self.name}{term.normal} equiped')

    def use_potion(self):
        self.newplist = list(dict.fromkeys(self.inv["potions"]))
        for self.w in self.newplist:
            print(f'{term.blue}Potion{term.normal} : {self.w} : {self.inv["potions"].count(self.w)} ')
        self.ii = input('|<>| ')
        puse = Potion(self.ii)
        puse.use_item()




class Sword:
    pass

class Armour:
    pass

class Potion:
    pinv = P_inv()
    def __init__(self,ptype):
        self.ptype = ptype
        self.name = finditem('potion','name',self.ptype)
        self.price = finditem('potion','price',self.ptype)
        self.desc = finditem('potion','desc',self.ptype)

    def use_item(self):
        if self.ptype not in self.pinv.inv['potions']:
            print("You don't have this item in your inventory")
        else:
            if self.name == 'Healing Potion':
                if player.HP == player.MAX_HP and self.pinv.inv['potions'].count(self.name) != 0 :
                    print("Can't use this potion")
                else:
                    self.oldHP = player.HP
                    player.HP += 5
                    self.pinv.inv['potions'].remove(self.name)
                    if player.HP > player.MAX_HP:
                        player.HP = player.MAX_HP
                    print(f"HP : {term.red}{self.oldHP}{term.normal} + 5 -> {term.green}{player.HP}{term.normal}")
            if self.name == 'Mana Potion':
                if player.MP == player.MAX_MP and self.pinv.inv['potions'].count(self.name) != 0 :
                    print("Can't use this potion")
                else:
                    self.oldMP = player.MP
                    player.MP += 5
                    self.pinv.inv['potions'].remove(self.name)
                    if player.MP > player.MAX_MP:
                        player.MP = player.MAX_MP
                    print(f"MP : {term.yellow}{self.oldMP}{term.normal} + 5 -> {term.blue}{player.MP}{term.normal}")






