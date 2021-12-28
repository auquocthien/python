class Parameters:
    __A = 0
    __Cps = 0
    __Cpm = 0
    __Cs = 0
    __Cm = 0

    def __init__(self):
        __A = 0
        __Cps = 0
        __Cpm = 0
        __Cs = 0
        __Cm = 0

    def copy(self, para):
        self.__A = para.__A
        self.__Cps = para.__Cps
        self.__Cpm = para.__Cpm
        self.__Cs = para.__Cs
        self.__Cm = para.__Cm

    def nhap(self):
        self.__A = int(input("set-up cost of manufacturer (A): "))
        self.__Cps = int(input("capacity of small truck (Cps): "))
        self.__Cpm = int(input("capacity of medium truck (Cpm): "))
        self.__Cs = int(input("transportation cost by small truck (Cs): "))
        self.__Cm = int(input("transportation cost by medium truck (Cm): "))

    def hienthi(self):
        print("A: {}, Cps:{}, Cpm:{}, Cs:{}, Cm:{}".format(self.__A, self.__Cps, self.__Cpm, self.__Cs, self.__Cm))

    def getA(self):
        return self.__A

    def getCps(self):
        return self.__Cps

    def getCpm(self):
        return self.__Cpm

    def getCs(self):
        return self.__Cs

    def getCm(self):
        return self.__Cm

    def setA(self, A):
        self.__A = A

    def setCps(self, Cps):
        self.__Cps = Cps

    def setCpm(self, Cpm):
        self.__Cpm = Cpm

    def setCs(self, Cs):
        self.__Cs = Cs

    def setCm(self, Cm):
        self.__Cm = Cm
