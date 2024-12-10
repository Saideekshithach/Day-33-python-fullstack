'''
#calendar
import calendar
year=2024
month=12
print(calendar.month(year,month))'''
'''import calendar
year=2025
print(calendar.calendar(year))'''

'''import calendar
year=int(input("enter the  year:"))
month=int(input("enter the month:"))
print(calendar.month(year,month))'''

#date

'''from datetime import date
a=date.today()
print(a)'''

'''from datetime import datetime
a=datetime.today()
print(a)'''

'''import datetime
a=datetime.datetime.now()
print(a)'''

'''import time
a=time.time()#epoch time
print(a)

b=time.localtime(a)
print(b)

print(f"today date is {b.tm_mday}-{b.tm_mon}-{b.tm_year}")
print(f"time is {b.tm_hour}-{b.tm_min}-{b.tm_sec}")
print(f"day is {b.tm_wday}-{b.tm_yday}-{b.tm_isdst}")'''

#random
'''*To generate random number in python ,randint function is used .This function is defined in random module.
*Python defines a set of functions that are used to generate or manipulate random numbers through the random module.'''
#random module
'''import random
a=random.sample(range(10,30),5)
print(*a)

#randint()
import random
a=random.randint(20,40)
print(a)

#choice
import random
a=[10,20,30,40,50]
b=random.choice(a)
print(b)

import random
a=["divya","bhavya","sai","deekshi"]
b=random.choice(a)
print(b)'''

while True:
    import random
    int(input("enter the number:"))
    dice=random.randint(1,6)
    print(dice)
    b=int(input('''roll again:
               1.yes
               2.no'''))
    if b==1:
        continue;
    elif b==2:
        print("exit")
        break;







