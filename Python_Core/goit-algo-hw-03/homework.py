import datetime
import random
import re
from datetime import datetime, timedelta

# # Завдання номер 1
# Варіант, коли дата ввдитться з клавіатури
def get_days_from_today():
    now = datetime.today()
    correct_input=False
    while not correct_input:
        try:
            date_str=input ("Введить дату в форматі'РРРР-ММ-ДД': ")
            date_str_object=datetime.strptime(date_str, '%Y-%m-%d')
            correct_input=True
        except ValueError:
            print("Формат дати не відповідає шаблону, повтрить ввід.", "\n")
    diffence=now.toordinal()-date_str_object.toordinal()
    if diffence < 0:
        return f"До введено дати ще {diffence*(-1)} днів."
    elif diffence==0:
        return f"Введено сьогодняшню дату, різніця дорівнює нулю."
    else:
        return f"Від введеної дати пройшло {diffence} днів."

print (get_days_from_today())
print("\n")

# #Варіат, коли дата передається до функції в якості аргументу 
def get_days_from_today1(date_str1: str):
    now1 = datetime.today()
    try:
        date_str_object1=datetime.strptime(date_str1, '%Y-%m-%d')
    except ValueError:
        print("Формат дати не відповідає шаблону.")
    diffence1=now1.toordinal()-date_str_object1.toordinal()
    if diffence1 < 0:
        return f"До введено дати ще {diffence1*(-1)} днів."
    elif diffence1==0:
        return f"Введено сьогодняшню дату, різніця дорівнює нулю."
    else:
        return f"Від введеної дати пройшло {diffence1} днів."

print (get_days_from_today1("1976-01-16"))
print("\n")

# Завдання номер 2
def get_numbers_ticket(min:int, max:int, quantity:int):
    list=[]
    if min < 1 or max > 1000:
        return f"Параметри не відповідають умовам"
    else:     
        while len(list) < quantity:
            num=random.randint(min,max)
            if num not in list:
                list.append(num)
        list.sort()
        return f"Ваші лотерейні числа: {list}"

print(get_numbers_ticket(1,49,5))
print("\n")

# Завдання номер 3
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
def normalize_phone(phone_number):
    pattrern=r"\d+"
    phone_number=''.join(re.findall(pattrern, phone_number))
    if len(phone_number)==10:
        phone_number='+38' + phone_number
    elif len(phone_number)==12:
        phone_number='+' + phone_number
    return phone_number

for numbers in raw_numbers:
    print(normalize_phone(numbers))
print("\n")

# Завдання номер 4
users = [
    {"name": "Anjelina Joly", "birthday": "1987.03.03"},
    {"name": "Bill Geits", "birthday": "1967.01.28"},
    {"name": "Brad Pitt", "birthday": "1979.02.01"}
]
def get_upcoming_birthdays (users=None):
    todays_day=datetime.today()
    birthdfay_list=[]
    for user in users:
        b_day=user["birthday"]
        b_day=str(todays_day.year)+b_day[4:]
        b_day=datetime.strptime(b_day, "%Y.%m.%d")
        week_day=b_day.weekday()
        diffr_days=b_day.toordinal()-todays_day.toordinal()
        if diffr_days>=0 and diffr_days<7:
            if week_day<5:
                birthdfay_list.append({'name':user['name'], 'birthday':b_day.strftime("%Y.%m.%d")})
            else:    
                if week_day == 6:
                    birthdfay_list.append({'name':user['name'], 'birthday':(b_day+timedelta(days=1)).strftime("%Y.%m.%d")})
                else:
                    if week_day == 5:
                       birthdfay_list.append({'name':user['name'], 'birthday':(b_day+timedelta(days=2)).strftime("%Y.%m.%d")})    
    return birthdfay_list 

print (get_upcoming_birthdays(users))
