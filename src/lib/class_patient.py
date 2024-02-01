from class_age_at_heart_attack import AgeAtHeartAttack
from class_alive_at_1 import AliveAtOne
from class_epss import Epss
from class_fractional_shortening import FractionalShortening
from class_group import Group
from class_lvdd import Lvdd
from class_mult import Mult
from class_name import Name
from class_pericardial_effusion import PericardialEffusion
from class_still_alive import StillAlive
from class_survival import Survival
from class_wall_motion_index import WallMotionIndex
from class_wall_motion_score import WallMotionScore


class Patient:
    
    # method's constructor
    def __init__(self, args):
        self.survival = Survival(args[0])
        self.stillAlive = StillAlive(args[1])
        self.ageAtHeartAttack = AgeAtHeartAttack(args[2])
        self.pericardialEffusion = PericardialEffusion(args[3])
        self.fractionalShortening = FractionalShortening(args[4])
        self.epss = Epss(args[5])
        self.lvdd = Lvdd(args[6])
        self.wallMotionScore = WallMotionScore(args[7])
        self.wallMotionIndex = WallMotionIndex(args[8])
        self.mult = Mult(args[9])
        self.name = Name(args[10])
        self.group = Group(args[11])
        self.aliveAtOne = AliveAtOne(args[12])
        
    # has been value assigned?
    def hasValue_Survival(self):
        return self.survival.IsNull() == False
    def hasValue_StillAlive(self):
        return self.stillAlive.IsNull() == False
    def hasValue_AgeAtHeartAttack(self):
        return self.ageAtHeartAttack.IsNull() == False
    def hasValue_PericardialEffusion(self):
        return self.pericardialEffusion.IsNull() == False
    def hasValue_FractionalShortening(self):
        return self.fractionalShortening.IsNull() == False
    def hasValue_Epss(self):
        return self.epss.IsNull() == False
    def hasValue_Lvdd(self):
        return self.lvdd.IsNull() == False
    def hasValue_WallMotionScore(self):
        return self.wallMotionScore.IsNull() == False
    def hasValue_WallMotionIndex(self):
        return self.wallMotionIndex.IsNull() == False
    def hasValue_Mult(self):
        return self.mult.IsNull() == False
    def hasValue_Name(self):
        return self.name.IsNull() == False
    def hasValue_Group(self):
        return self.group.IsNull() == False
    def hasValue_AliveAtOne(self):
        return self.aliveAtOne.IsNull() == False

    # getters
    def get_Survival(self):
        return self.survival.GetValue()
    def get_StillAlive(self):
        return self.stillAlive.GetValue()
    def get_AgeAtHeartAttack(self):
        return self.ageAtHeartAttack.GetValue()
    def get_PericardialEffusion(self):
        return self.pericardialEffusion.GetValue()
    def get_FractionalShortening(self):
        return self.fractionalShortening.GetValue()
    def get_Epss(self):
        return self.epss.GetValue()
    def get_Lvdd(self):
        return self.lvdd.GetValue()
    def get_WallMotionScore(self):
        return self.wallMotionScore.GetValue()
    def get_WallMotionIndex(self):
        return self.wallMotionIndex.GetValue()
    def get_Mult(self):
        return self.mult.GetValue()
    def get_Name(self):
        return self.name.GetValue()
    def get_Group(self):
        return self.group.GetValue()
    def get_AliveAtOne(self):
        return self.aliveAtOne.GetValue()

    # setters
    def set_Survival(self, value):
        self.survival.SetValue(value)
    def set_StillAlive(self, value):
        return self.stillAlive.SetValue(value)
    def set_AgeAtHeartAttack(self, value):
        return self.ageAtHeartAttack.SetValue(value)
    def set_PericardialEffusion(self, value):
        return self.pericardialEffusion.SetValue(value)
    def set_FractionalShortening(self, value):
        return self.fractionalShortening.SetValue(value)
    def set_Epss(self, value):
        return self.epss.SetValue(value)
    def set_Lvdd(self, value):
        return self.lvdd.SetValue(value)
    def set_WallMotionScore(self, value):
        return self.wallMotionScore.SetValue(value)
    def set_WallMotionIndex(self, value):
        return self.wallMotionIndex.SetValue(value)
    def set_Mult(self, value):
        return self.mult.SetValue(value)
    def set_Name(self, value):
        return self.name.SetValue(value)
    def set_Group(self, value):
        return self.group.SetValue(value)
    def set_AliveAtOne(self, value):
        return self.aliveAtOne.SetValue(value)

    # obtain the number of boolean variables that haven't been assigned
    def getMissing_Boolean(self):
        missing = 0
        if (not self.hasValue_StillAlive()):
            missing += 1
        return missing

    # obtain the number of numeric variables that haven't been assigned
    def getMissing_Numeric(self):
        missing = 0
        if (not self.hasValue_Survival()):
            missing += 1
        if (not self.hasValue_AgeAtHeartAttack()):
            missing += 1
        if (not self.hasValue_FractionalShortening()):
            missing += 1
        if (not self.hasValue_Epss()):
            missing += 1
        if (not self.hasValue_Lvdd()):
            missing += 1
        if (not self.hasValue_WallMotionIndex()):
            missing += 1
        if (not self.hasValue_PericardialEffusion()):
            missing += 1
        return missing

    def show(self):
        print self.get_Survival(), self.get_StillAlive(), self.get_AgeAtHeartAttack(), self.get_PericardialEffusion(), self.get_FractionalShortening(), self.get_Epss(), self.get_Lvdd(), self.get_WallMotionScore(), self.get_WallMotionIndex(), self.get_Mult(), self.get_Name(), self.get_Group(), self.get_AliveAtOne()
