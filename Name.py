from Database import Database


class Name:
    def __init__(self, name, year, gender, count):
        __name = ""
        __year = 0
        __gender = ""
        __count = 0

    @staticmethod
    def readNames(cls):
        cls.connect()
        names = Database.readNames(cls)
        return names



    def getName(self):
        return self.__name

    def getYear(self):
        return self.__year

    def getGender(self):
        return self.__gender

    def getCount(self):
        return self.__count

    def setName(self, newName):
        self.__name = newName

    def setYear(self, newYear):
        self.__year = newYear

    def setGender(self, newGender):
        self.__gender = newGender

    def setCount(self, newCount):
        self.__count = newCount





