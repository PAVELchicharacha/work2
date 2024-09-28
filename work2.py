#1 задача
from calendar import day_abbr
from datetime import datetime
from tkinter.font import names


class Calendar:
    def __init__ (self, year, month, day):
        self.__day=day
        self.__year=year
        self.__month=month
    def inc_year (self):
        self.__year+=1
    def dec_day(self):
        self.__day-=2
    def print(self):
        print(self.__year, self.__month,self.__day)

cal=Calendar (12,2,2024)
cal. print()
cal.inc_year()
cal.print()
cal.dec_day()
cal.print()

# 2 задача

class BirthDay(Calendar):
    def __init__(self, fio, pnumber, bday, year, month, day):
        super().__init__(year, month, day)
        self.__day = day
        self.__year = year
        self.__month = month
        self.__FIO=fio
        self.__PNumber=pnumber
        self.__BDay=bday
    def Before_Next_Bday(self,year2,month2,day2):
        self.__year2=year2
        self.__month2=month2
        self.__day2=day2
        self.__year2-=self.__year
        self.__month2-=self.__month
        self.__day2-=self.__day
    def print(self):
        print(self.__year2, self.__month2, self.__day2)

NBDay=BirthDay("oleg olegovich",89212645045,"yes",2024,12,10)
NBDay.Before_Next_Bday(2200,12,14)
print("до дня ржения ГГ ММ ДД")
NBDay.print()

# 3задача

class Dumaem:
    def __init__(self,name,coast,s):
        self.__name=name
        self.__coast=coast
        self.__s=s
    def true(self,coast,s):
        self.__coast = coast
        self.__s = s
        q = 100 * self.__s / self.__coast
        awnser = 0.7 * q
        print(awnser,"true")
    def false(self,coast,s):
        self.__coast = coast
        self.__s = s
        q = 100 * self.__s / self.__coast
        awnser = 1.5 * q
        print(awnser,"false")





mb=Dumaem("oleg",10,30)
mb.true(12,2)
# mb.print()
mb.false(11,11)
# mb.print()