from collections import UserList, UserDict
from datetime import datetime
from colorama import Fore
import re
import pickle

class Name:
    def __init__(self, name):
        self.name=name

    def setName(self,name):
        self.name=name
        return f"{Fore.YELLOW}Імʼя {Fore.GREEN}{name}{Fore.YELLOW} встановлено{Fore.RESET}"
    
    def getName(self):
        return self.name
    
    def changeName(self, name):
        self.setName(name)
        return f"{Fore.YELLOW}Імʼя змінено на {Fore.GREEN}{name}{Fore.RESET}"
    
    def __str__(self) -> str:
        return self.name
    
class Birthday:
    def __init__(self) -> datetime:
        self.birthday=datetime
    
    def setBirthday(self, birthday):
        self.birthday=datetime.strptime(birthday, '%d.%m.%Y')
        return f"{Fore.YELLOW}День народження {Fore.GREEN}{birthday} {Fore.YELLOW}встановлено{Fore.RESET}"

    def getBirthday(self):
        return self.birthday
    
    def changeBirthday(self, birthday):
        self.setBirthday(birthday)
        return f"{Fore.YELLOW}День народження змінено на {Fore.GREEN}{birthday}{Fore.RESET}"
    
    def findBirthday(self, birthday):
        return birthday == self.birthday.strftime('%d.%m.%Y')
    
    def __str__(self):
        return f"{self.birthday.strftime('%d.%m.%Y')}"
    
class Phone(UserList):

    def normalizePone(self, phone): # Нормализатор номера телефона
        if len(phone) == 12:
            new_phone = "+" + phone
            return new_phone
        elif len(phone) < 12:
            new_phone = "+38" + phone   
            return new_phone
        return phone

    def setPhone(self,phone):
        if self.normalizePone(phone) not in self.data:
            self.data.append(self.normalizePone(phone))
            return f"{Fore.YELLOW}Номер {Fore.GREEN}{self.normalizePone(phone)} {Fore.YELLOW}добавлено.{Fore.RESET}"
        else:
            return f"{Fore.RED}Номер {Fore.GREEN}{self.normalizePone(phone)} {Fore.RED}вже існує.{Fore.RESET}"

    def getPhone(self): # возвращает №-ра телефонов списком -> List
        return self.data
    
    def getPhones(self): # возвращает №-ра телефонов одной строкой -> Str
        return f"{'; '.join(self)}" 
    
    def delPhone(self, phone):
        self.data.remove(self.normalizePone(phone))
        return f"{Fore.YELLOW}Номер {Fore.GREEN}{self.normalizePone(phone)} {Fore.YELLOW}видалено.{Fore.RESET}"

    def findPhone(self, phone):
        return self.normalizePone(phone) in self.data

    def changePhone(self,phone1, phone2):
        self.data.remove(self.normalizePone(phone1))
        self.setPhone(phone2)
        return f"{Fore.YELLOW}Номер {Fore.GREEN}{self.normalizePone(phone1)} {Fore.YELLOW}було змінено на {Fore.GREEN}{self.normalizePone(phone2)}{Fore.RESET}"

class Record:
    def __init__(self, name):
        self.name=Name(name)
        self.phone=Phone()
        self.birthday=Birthday()

    def setName(self, name):
        self.name=Name(name)
        return f"{Fore.YELLOW}Імʼя {Fore.GREEN}{name} {Fore.YELLOW}встановлено{Fore.RESET}"

    def getName(self):
        return self.name.getName()
    
    def changeName(self, name):
        self.name.setName(name)
        return f"{Fore.YELLOW}Імʼя змінено на {Fore.GREEN}{name}{Fore.RESET}"
    
    def setBirthday(self, b_day):
        return self.birthday.setBirthday(b_day)

    def getBirthday(self):
        return self.birthday.getBirthday()
    
    def changeBirthday(self, birthday):
        self.birthday.setBirthday(birthday)
        return f"{Fore.YELLOW}День народження змінено на {Fore.GREEN}{birthday}{Fore.RESET}"

    def setPhone(self,phone):
        return self.phone.setPhone(phone)

    def changePhone(self, phone1, phone2):
        # if self.phone.normalizePone(phone1) in self.getPhone(): # 2-й варіант перевірки наявності телефону
        if self.phone.findPhone(phone1):
            return self.phone.changePhone(phone1, phone2)
        else:
            return f"{Fore.YELLOW}Tелефонний номер {Fore.GREEN}{self.phone.normalizePone(phone1)} {Fore.YELLOW}не знайдерно{Fore.RESET}"

    def delPhone(self, phone):
        if self.phone.findPhone(phone):
            return self.phone.delPhone(phone)
        else:
            return f"{Fore.RED}Tелефонний номер {Fore.GREEN}{self.phone.normalizePone(phone)} не знайдерно{Fore.RESET}"

    def getPhone(self):
        return self.phone.data

    def getPhones(self):
        return f"{'; '.join(self.phone)}" 

    def findPhone(self, phone):
        if self.phone.findPhone(phone):
            return f"{Fore.YELLOW}Номер {Fore.GREEN}{self.phone.normalizePone(phone)} {Fore.YELLOW}належить користувачу {Fore.GREEN}{self.getName()}.{Fore.RESET}"
            # return True
        else:
            return f"{Fore.RED}Номер {Fore.GREEN}{self.phone.normalizePone(phone)} {Fore.RED}не знайдено.{Fore.RESET}"
            # return False
    
    def findBirthday(self, birthday):
        if self.birthday.findBirthday(birthday):
            return f"{Fore.YELLOW}День нарподження {Fore.GREEN}{birthday} {Fore.YELLOW}належить користувачу {Fore.GREEN}{self.getName()}{Fore.RESET}"
        else:
            return f"{Fore.RED}День нарподження {Fore.GREEN}{birthday} {Fore.RED}не знайдено{Fore.RESET}"

    def showRecord(self):
        if len(str(self.birthday.getBirthday())) == 19:
            return f"{Fore.GREEN}{self.getName()}{Fore.RESET}; тел.: {self.phone.getPhones()}, д.н.: {self.birthday.getBirthday().strftime('%d.%m.%Y')}."
        else:
            return f"{Fore.GREEN}{self.getName()}{Fore.RESET}; тел.: {self.phone.getPhones()}."
    
    def __str__(self):
        if len(str(self.birthday.getBirthday())) == 19:
            return f"{self.getName()}; {self.phone.getPhones()}; {self.birthday.getBirthday().strftime('%d.%m.%Y')}"
        else:
            return f"{self.getName()}; {self.phone.getPhones()}"

class AddressBook(UserDict):

    def addRecord(self, record):
        self.data[record]=record   
        return f"{Fore.YELLOW}Запис {Fore.GREEN}{record.getName()} {Fore.YELLOW}доданий до адресної книги.{Fore.RESET}"
    
    def printBook(self):
        id=1
        for rec in self.data:
            if len(str(self.data[rec].getBirthday())) == 19:
                print(f"{id:3}. {self.data[rec].getName():12} тел. {self.data[rec].getPhones()}\n{' ':17} д.н. {self.data[rec].getBirthday().strftime('%d.%m.%Y')}")
                id+=1
            else:
                print(f"{id:3}. {self.data[rec].getName():12} тел. {self.data[rec].getPhones()}")
                id+=1

    def select(self, name):
        found_status=False
        for n in self.data:
            if self.data[n].getName() == name: # Запис знайдено
                found_status=True
                return self.data[n]
    
    def ifExist(self, name):
        found=False
        for n in self.data:
            if self.data[n].getName() == name:
                found = True
        return found

    def delete(self,name):
        if self.ifExist(name):
            temp_book=AddressBook()
            for n in self.data:
                if not str(self.data[n].getName()) == name:
                   temp_book[n]=self.data[n]
            print(f"{Fore.YELLOW}Запис {Fore.GREEN}{name} {Fore.YELLOW}видалено.{Fore.RESET}")
            return temp_book
        else:
            print(f"{Fore.RED}Запис {Fore.GREEN}{name} {Fore.RED}не знайдено.{Fore.RESET}")
            return self

    def findPhone(self, phone):
        for rec in self.data:
            if self.data[rec].phone.findPhone(phone):
                return self.data[rec].findPhone(phone)
        return f"Номер {phone} відсутній"
            # print(self.data[rec].phone.findPhone(phone))
    
    def findBirthday(self, birthday): # ++ добавити перевірку формату
        for rec in self.data:
            if len(str(self.data[rec].getBirthday())) == 19:
                if self.data[rec].birthday.findBirthday(birthday):
                    return self.data[rec].findBirthday(birthday)
        return f"{Fore.RED}День народження {Fore.GREEN}{birthday} {Fore.RED}відсутній.{Fore.RESET}"
    

# ================================ Функції логики боту ==================================#
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# ------- додає Запис до Адресної книги
def addToBook(args, record:AddressBook):
    record=record.addRecord(args)
    return record

# ------- видає список днів народження з Адресної книги, які відбудуться протягом 7 днів
def getUpcommingBirthdays(users): # ++
    today=datetime.today()
    birthday_list=[]
    for user in users:
        if len(str(users[user].getBirthday())) == 19:
            tempt_b_day=datetime(year=today.year, month=user.getBirthday().month, day=user.getBirthday().day)
            diffr_days=tempt_b_day.toordinal()-today.toordinal()
            if diffr_days >= 0 and diffr_days <7:
                birthday_list.append({'name':user.getName(), 'birthday':tempt_b_day.strftime("%d.%m.%Y")})
    if birthday_list:
        print(f"{Fore.YELLOW}Список найближчих іменинників:{Fore.RESET}")
        # lambda x: x in birthday_list, (map((print(birthday_list[x]['name'], ' - ', birthday_list[x]['birthday'])), birthday_list))   
        for i in birthday_list:
            print(f"{Fore.GREEN}{i['name']}{Fore.RESET} - {i['birthday']}")
        return birthday_list
    else:
        print('Найближчими днями іменинників - немає')
        return birthday_list

# ------- виводить справку по командам
def help(file):
    with open(file, 'r', encoding="UTF-8") as fh:
        print(fh.read())

# ------- видаляє Запис з Адресної книги
def delrec(name, book):
    book=book.delete(name)   
    return book

# ------- додає нову Запис до Адресної книги в залежності від кількості аргументів (імʼя, тел., д/p)
def createRecord(args, book): # додати перевірку формату тел и др
    if len(args) == 1:
        args[0]=Record(args[0])
        return addToBook(args[0], book)
    elif len(args) == 2:
        args[0]=Record(args[0])
        args[0].setPhone(args[1])
        return addToBook(args[0], book)
    elif len(args) == 3:
        args[0]=Record(args[0])
        args[0].setPhone(args[1])
        args[0].setBirthday(args[2])
        return addToBook(args[0], book)

# ------- перевірка чи строка є телефонним номером
def is_ph_number(number:str) ->bool:
    if number.isdigit() and (10<=len(number)<=12):
        return True
    else:
        return False

# ------- перевірка чи строка є датою
def is_date(date:str) ->bool:
    # date=''.join(re.findall(r"\d{2}\.\d{2}\.\d{4}", date))
    if ''.join(re.findall(r"\d{2}\.\d{2}\.\d{4}", date)):
        return True
    else:
        return False

# ------- виводить імʼя активного запису під час його редагування (під час вводу команд).
def recMode(rec, book):
    def RecModeMane(record):
        return f"[ {Fore.GREEN}{name.getName()}{Fore.RESET} ] >>> "
    print(f"{Fore.GREEN}Режим редагування запису!{Fore.RESET}\n")
    name=book.select(rec) # тимчасовий запис для редагування
    while True:
        user_input = input(RecModeMane(name))
        command, *args = parse_input(user_input)
        if command == "quit":
            break
        elif command == "change_name" and len(args)==1:
            print(name.setName(args[0]))
        elif command == "set_phone" and len(args)==1 and is_ph_number(args[0]):
            print(name.setPhone(args[0]))
        elif command == "change_phone" and len(args)==2 and is_ph_number(args[0]) and is_ph_number(args[1]): 
            print(name.changePhone(args[0], args[1]))
        elif command == "delete_phone" and len(args)==1 and is_ph_number(args[0]):
            print(name.delPhone(args[0]))
        elif command == "set_birthday" and len(args)==1 and is_date(args[0]):
            print(name.setBirthday(args[0]))
        elif command == "print":
            print(name.showRecord())
        elif command == "help":
            help('help_rec_mode.txt')
        else:
            print(warning())
    return book

# ------- виводить повідомлення про помилку
def warning():
    return f"{Fore.RED}Error:{Fore.RESET} Невірна команда або аргумент(-ти)\n{' ':7}Для довідки - введить {Fore.GREEN}help{Fore.RESET}\n"

# ------- серіалізує книгу у файл
def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as file:
        pickle.dump(book, file)

# ------- десеріалізує книгу з файлу
def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return AddressBook()  # Повернення нової адресної книги, якщо файл не знайдено

def main():
    book = load_data() #Завантаження збереженої книги
    print(f"{Fore.GREEN}Welcome to the assistant bot!{Fore.RESET}")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit", "quit"]:
            print(f"{Fore.GREEN}Good bye!{Fore.RESET}")
            save_data(book)
            break
        elif command == "hello":
            print("How can I help you?\n(type HELP for the list of commands)")
        elif command == "delete":
            if args:
                book=book.delete(args[0])
            else:
                print(f"Не введено імʼя.")
            # delrec(args[0], book)
        elif command == "all":
            book.printBook()
        elif command == "birthdays":
            getUpcommingBirthdays(book)
        elif command == "help":
            help('help.txt')
        elif command == "change_name" and len(args)==2:
            print(book.select(args[0]).changeName(args[1]))
        elif command == "change_phone" and len(args)==3 and is_ph_number(args[1]) and is_ph_number(args[2]):
            print(book.select(args[0]).changePhone(args[1], args[2]))
        elif command == "find_phone" and len(args)==1 and is_ph_number(args[0]): 
            print(book.findPhone(args[0]))
        elif command == "delete_phone" and len(args)==2 and is_ph_number(args[1]):
            print(book.select(args[0]).delPhone(args[1]))
        elif command == "set_phone" and len(args)==2 and is_ph_number(args[1]):
            print(book.select(args[0]).setPhone(args[1]))
        elif command == "print" and len(args)==1:
            if book.ifExist(args[0]):
                print(book.select(args[0]).showRecord())
            else:
                print(f"Запис {args[0]} не знайдено.")
        elif command == "add" and len(args)>=1:
            print(createRecord(args, book))
        elif command == "find_birthday" and len(args)==1 and is_date(args[0]):
            print(book.findBirthday(args[0]))
        elif command == "change_birthday" and len(args)==2 and is_date(args[1]):
            print(book.select(args[0]).birthday.changeBirthday(args[1]))
        elif command == "set_birthday" and len(args)==2 and is_date(args[1]):
            print(book.select(args[0]).setBirthday(args[1]))
        elif command == "record_mode" and len(args)==1:
            if book.select(args[0]):
                recMode(args[0], book)
            else:
                print(f"Імʼя {args[0]} не знайдено.")
        else:
            print(warning())

if __name__ == "__main__":
    main()