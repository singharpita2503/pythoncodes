"""correct_pin = 1190
balance = 2000
attempts = 3

while attempts > 0:
    try:
        pin = int(input("Enter PIN: "))

        if pin != correct_pin:
            attempts -= 1
            print("Wrong PIN. Attempts left:", attempts)
            continue

        amount = int(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount")
        elif amount > balance:
            print("Insufficient balance")
        else:
            balance -= amount
            print("Collect cash")
            print("Remaining balance:", balance)

        print("Remove your card")
        break

    except ValueError:
        print("Invalid input. Numbers only")

else:
    print("ATM blocked due to multiple wrong attempts")

print("Thank you")"""

import datetime
datetime_obj= datetime.datetime.now()
print(datetime_obj)

date_obj=datetime.date.today()
print(date_obj)
from datetime import datetime
now=datetime.now().time()
print(now)

time_obj=now.strftime("%H:%M:%S")
print(time_obj)

import calendar
#calendar.setfirstweekday(calendar.SUNDAY)
year=int(input("Enter your year: "))
#month=int(input("Enter your month: "))
#calendar_obj=calendar.calendar.()
#print(calendar.calendar(year))

month=int(input("Enter Your month: "))
#day=int(input("Enter your day: "))
print(calendar.month(year,month))

import datetime
D=int(input("Enter your Birth Date: "))
M=int(input("Enter your Birth Month:"))
Y=int(input("Enter your Birth Date: "))
print(datetime.datetime(Y,M,D).strftime("%A"))

