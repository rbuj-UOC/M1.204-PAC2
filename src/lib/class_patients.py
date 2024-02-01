from arithmetic_mean import arithmeticMean
from class_patient import Patient
from numpy import *
from ranging import *

class Patients:
    
    # method's constructor
    def __init__(self, nomFitx):
        print "Pacients:"
        print "llegint dades del fitxer..."
        lines = [(l.strip()).split(",") for l in (open(nomFitx).readlines())]
        self.patients = []
        self.patients_train = []
        self.patients_prediction = []
        # descartar els pacients que no han superat el temps minim d'obsebacio i
        # figuren com a vius
        print "Descartant els pacients que no han superat el temps minim d'observacio i figuren com a vius..."
        for args in lines:
            patient = Patient(args)
            self.patients.append(patient)
            if ((patient.get_Survival() < 12.0) & (patient.get_StillAlive() == True)):
                self.patients_prediction.append(patient)
                # patient.show()
            else:
                self.patients_train.append(patient)
        # detalls variables assignades/no assignades
        print "Nombre de variables booleans inicialment no assignades:", self.numMissing_Boolean()
        print "Nombre de variables numeriques inicialment no assignades:", self.numMissing_Numeric()
        # corregir els valors numerics que falten
        self.__fixMissing(arithmeticMean)
        # ranging
        self.__ranging()
        print "Nombre de pacients:", self.size()
        print
 
    # return the patients's number
    def size(self):
        return len(self.patients)

    def __listNotNull_Survival(self):
        aList = []
        for patient in self.patients:
            if patient.hasValue_Survival():
                aList.append(patient.get_Survival())
        return aList
    def __listNotNull_AgeAtHeartAttack(self):
        aList = []
        for patient in self.patients:
            if patient.hasValue_AgeAtHeartAttack():
                aList.append(patient.get_AgeAtHeartAttack())
        return aList
    def __listNotNull_FractionalShortening(self):
        aList = []
        for patient in self.patients:
            if patient.hasValue_FractionalShortening():
                aList.append(patient.get_FractionalShortening())
        return aList
    def __listNotNull_Epps(self):
        aList = []
        for patient in self.patients:
            if patient.hasValue_Epss():
                aList.append(patient.get_Epss())
        return aList
    def __listNotNull_Lvdd(self):
        aList = []
        for patient in self.patients:
            if patient.hasValue_Lvdd():
                aList.append(patient.get_Lvdd())
        return aList
    def __listNotNull_WallMotionIndex(self):
        aList = []
        for patient in self.patients:
            if patient.hasValue_WallMotionIndex():
                aList.append(patient.get_WallMotionIndex())
        return aList
    def __listNotNull_PericardialEffusion(self):
        aList = []
        for patient in self.patients:
            if patient.hasValue_PericardialEffusion():
                aList.append(patient.get_PericardialEffusion())
        return aList
    
    # fix the missing values
    def __fixMissing(self, funcFixedValue):
        print "Tractant variables numeriques sense assignar: assignar mitja aritmetica..."
        fixedValue_Survival = funcFixedValue(self.__listNotNull_Survival())
        fixedValue_AgeAtHeartAttack = funcFixedValue(self.__listNotNull_AgeAtHeartAttack())
        fixedValue_FractionalShortening = funcFixedValue(self.__listNotNull_FractionalShortening())
        fixedValue_Epss = funcFixedValue(self.__listNotNull_Epps())
        fixedValue_Lvdd = funcFixedValue(self.__listNotNull_Lvdd())
        fixedValue_WallMotionIndex = funcFixedValue(self.__listNotNull_WallMotionIndex())
        fixedValue_PericardialEffusion = funcFixedValue(self.__listNotNull_PericardialEffusion())
        for idx in range(len(self.patients)):
            if (not self.patients[idx].hasValue_Survival()):
                self.patients[idx].set_Survival(fixedValue_Survival)
            if (not self.patients[idx].hasValue_AgeAtHeartAttack()):
                self.patients[idx].set_AgeAtHeartAttack(fixedValue_AgeAtHeartAttack)
            if (not self.patients[idx].hasValue_FractionalShortening()):
                self.patients[idx].set_FractionalShortening(fixedValue_FractionalShortening)
            if (not self.patients[idx].hasValue_Epss()):
                self.patients[idx].set_Epss(fixedValue_Epss)
            if (not self.patients[idx].hasValue_Lvdd()):
                self.patients[idx].set_Lvdd(fixedValue_Lvdd)
            if (not self.patients[idx].hasValue_WallMotionIndex()):
                self.patients[idx].set_WallMotionIndex(fixedValue_WallMotionIndex)
            if (not self.patients[idx].hasValue_PericardialEffusion()):
                self.patients[idx].set_PericardialEffusion(fixedValue_PericardialEffusion)

    # ranging
    def __ranging(self):
        print "Tractant valor de les variables: ranging..."
        # pericardial-effusion ja esta dins del rang [0,1]
        max_Survival, min_Survival = limitValues(self.__listNotNull_Survival())
        max_AgeAtHeartAttack, min_AgeAtHeartAttack = limitValues(self.__listNotNull_AgeAtHeartAttack())
        max_FractionalShortening, min_FractionalShortening = limitValues(self.__listNotNull_FractionalShortening())
        max_Epss, min_Epss = limitValues(self.__listNotNull_Epps())
        max_Lvdd, min_Lvdd = limitValues(self.__listNotNull_Lvdd())
        max_WallMotionIndex, min_WallMotionIndex = limitValues(self.__listNotNull_WallMotionIndex())
        for idx in range(len(self.patients)):
            self.patients[idx].set_Survival((self.patients[idx].get_Survival() - min_Survival) / (max_Survival - min_Survival))
            self.patients[idx].set_AgeAtHeartAttack((self.patients[idx].get_AgeAtHeartAttack() - min_AgeAtHeartAttack) / (max_AgeAtHeartAttack - min_AgeAtHeartAttack))
            self.patients[idx].set_FractionalShortening((self.patients[idx].get_FractionalShortening() - min_FractionalShortening) / (max_FractionalShortening - min_FractionalShortening))
            self.patients[idx].set_Epss((self.patients[idx].get_Epss() - min_Epss) / (max_Epss - min_Epss))
            self.patients[idx].set_Lvdd((self.patients[idx].get_Lvdd() - min_Lvdd) / (max_Lvdd - min_Lvdd))
            self.patients[idx].set_WallMotionIndex((self.patients[idx].get_WallMotionIndex() - min_WallMotionIndex) / (max_WallMotionIndex - min_WallMotionIndex))

    # return total of missing assignaments of boolean variables
    def numMissing_Boolean(self):
        total = 0
        for patient in self.patients:
            total += patient.getMissing_Boolean()
        return total

    # return total of missing assignaments of numeric variables
    def numMissing_Numeric(self):
        total = 0
        for patient in self.patients:
            total += patient.getMissing_Numeric()
        return total

    # to matrix
    def convertToProcessData(self, num):
        myData  = zeros([self.size(), num], float)
        myClass = zeros([self.size(), 1], int)
        for idx in range(len(self.patients)):
            if (num >= 1):
                myData[idx][0] = self.patients[idx].get_Survival()
            if (num >= 2):
                myData[idx][1] = self.patients[idx].get_AgeAtHeartAttack()
            if (num >= 3):
                myData[idx][2] = self.patients[idx].get_WallMotionIndex()
            if (num >= 4):
                myData[idx][3] = self.patients[idx].get_FractionalShortening()
            if (num >= 5):
                myData[idx][4] = self.patients[idx].get_Epss()
            if (num >= 6):
                myData[idx][5] = self.patients[idx].get_Lvdd()
            if (num == 7):
                myData[idx][6] = self.patients[idx].get_PericardialEffusion()
            myClass[idx] = self.patients[idx].get_StillAlive()
        return myData, myClass

    # get the variable's name
    def getVariablesName(self, indexs):
        variables_name  = ["Survival", "AgeAtHeartAttack", "WallMotionIndex", "FractionalShortening", "Epss", "Lvdd", "PericardialEffusion"]
        answer = []
        for i in range(len(indexs)):
            answer.append(variables_name[indexs[i]])
        return answer

    def show(self):
        for patient in self.patients:
            patient.show()
