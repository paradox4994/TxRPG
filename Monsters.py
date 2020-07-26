import random
import xml.etree.ElementTree as ET




class Monsters:
    def __init__(self,name):
        self.name = name
        mytree = ET.parse('entities.xml')
        myroot = mytree.getroot()

        self.all_monster = myroot.findall('monster')
        for m in self.all_monster:
            if m.find('type').text == self.name:
                self.type = m.find('type').text
                self.HP = int(m.find('HP').text)
                self.MP = int(m.find('MP').text)
                self.STR = int(m.find('STR').text)
                self.INT = int(m.find('INT').text)
                self.DEX = int(m.find('DEX').text)
                self.DEF = int(m.find('DEF').text)
                self.LUCK = random.randint(1, 9)
                self.XP_AWARDED = int(m.find('XP_AWARDED').text)
                self.GOLD_AWARDED = int(m.find('GOLD_AWARDED').text)
                self.description = m.find('description').text
                self.category = m.find('category').text
                self.location = m.find('location').text