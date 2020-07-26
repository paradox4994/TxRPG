import random

class Dice:
    def Roll_attack(self,STR,DEF):
        self.STR = STR
        self.DEF = DEF
        DI = random.randint(0,12)
        RSTR = random.randint(STR-2,STR)
        RDEF = random.randint(DEF-2,DEF)
        roll = random.randint(1,3)
        DMG = ((RSTR + DI) * roll) - RDEF
        if(DMG <= 0):
            return 0
        else:
            return DMG
    def Roll_magic(self,INT,DEF,TYPE,TYPE_DMG):
        self.INT = INT
        self.DEF = DEF
        self.TYPE = TYPE
        self.TYPE_DMG = TYPE_DMG
        RINT = random.randint(0,INT)
        RDEF = random.randint(0,DEF)
        roll = random.randint(0,12)
        DMG = (RINT + (roll + TYPE_DMG) - RDEF)
        if (DMG <= 0):
            return 0
        else:
            return DMG