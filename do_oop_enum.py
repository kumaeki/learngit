from enum import Enum,unique

Month =Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))


for name,menber in Month.__members__.items():
    print(name,"=>",menber,',',menber.value)


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


print(Weekday.Mon)
print(Weekday.Tue.value)
print(Weekday(5))
