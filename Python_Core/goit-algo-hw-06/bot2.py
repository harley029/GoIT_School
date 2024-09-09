from collections import UserList, UserDict

class Name:
    def __init__(self, name):
        self.name=name

    def setName(self,name):
        self.name=name
    
    def getName(self):
        return self.name
    
    def changeName(self, name):
        self.setName(name)
        return f"Імʼя змінено на {name}"
    
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
            return f"Номер {self.normalizePone(phone)} добавлено."
        else:
            return f"Номер {self.normalizePone(phone)} вже існує."

    def getPhone(self): # возвращает №-ра телефонов списком -> List
        return self.data
    
    def getPhones(self): # возвращает №-ра телефонов одной строкой -> Str
        return f"{'; '.join(self)}" 
    
    def delPhone(self, phone):
        self.data.remove(self.normalizePone(phone))
        return f"Номер {self.normalizePone(phone)} видалено."

    def findPhone(self, phone):
        return self.normalizePone(phone) in self.data

    def changePhone(self,phone1, phone2):
        self.data.remove(self.normalizePone(phone1))
        self.setPhone(phone2)
        return f"Номер {self.normalizePone(phone1)} було змінено на {self.normalizePone(phone2)}"

class Record:
    def __init__(self, name):
        self.name=Name(name)
        self.phone=Phone()

    def setName(self, name):
        self.name=Name(name)

    def getName(self):
        return self.name.getName()
    
    def changeName(self, name):
        self.name.setName(name)
        return f"Імʼя змінено на {name}"

    def setPhone(self,phone):
        self.phone.setPhone(phone)

    def changePhone(self, phone1, phone2):
        return self.phone.changePhone(phone1, phone2)

    def delPhone(self, phone):
        return self.phone.delPhone(phone)

    def getPhone(self):
        return self.phone.data

    def getPhones(self):
        return f"{'; '.join(self.phone)}" 

    def findPhone(self, phone):
        if self.phone.findPhone(phone):
            print(f"Номер {self.phone.normalizePone(phone)} належить користувачу {self.getName()}.")
            # return True
        else:
            print(f"Номер {self.phone.normalizePone(phone)} не знайдено.")
            # return False

    def showRecord(self):
        return f"{self.getName()}; тел.: {self.phone.getPhones()}"
    
class AddressBook(UserDict):

    def addRecord(self, record):
        self.data[record]=record   
        return f"Запис {record.getName()} доданий до адресної книги."
    
    def printBook(self):
        for rec in self.data:
            print(self.data[rec].showRecord())

    def find(self, name):
        found_status=False
        for n in self.data:
            if self.data[n].getName() == name:
                # print('Запис знайдено')
                found_status=True
                return self.data[n]
        if not found_status:
            print(f"Запис на імʼя {name} не знайдено.")
            return Record('')

    def delete(self,name):
        temp_book=AddressBook()
        for n in self.data:
            if not self.data[n].getName() == name.getName():
               temp_book[n]=self.data[n]
        return temp_book

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def addToBook(args, record:AddressBook):
    record=record.addRecord(args)
    return record

# Створення нової адресної книги
book=AddressBook()  
# Створення запису для Jill
jill=Record('Jill')
jill.setPhone('0502345678')
jill.setPhone('380635654323')
print(addToBook(jill,book))
input('Для продовження натиснить ENTER')
# Створення запису для John
john_record=Record('John')
john_record.setPhone('0989309711')
john_record.setPhone('380507331167')
# Додавання запису John до адресної книги
print(addToBook(john_record, book))
# Створення та додавання нового запису для Jane без виводу повыдомлення
jane_record = Record("Jane")
jane_record.setPhone("9876543210")
addToBook(jane_record, book)
print()
input('Для виводу адресної книги - натиснить ENTER')
book.printBook()
print()
# пошук Jill в адресної книзі
a=book.find('Jill')
input('Для видалення запису Jill та виводу всієї книги натиснить ENTER')
# видалення Jill з адресної книги
book=book.delete(a)
book.printBook()

# ----------------------------------------------------------------------
# 
# Це команди для перевірки всіх існуючих методів по класах. Всі працюють.
# print(book.data[john_record].delPhone('0507331167'))
# print(book.data[john_record].getPhone())
# a=Record('Johan')
# print(a.name.getName())
# print(a.name.changeName('Alex'))
# print(a.name.getName())

# a.setName('Tanya')
# print(a.getName())
# print(a.changeName('Qwerty'))
# print(a.getName())

# print(a.phone.setPhone('0989309711'))
# print(a.phone.setPhone('380989309711'))
# print(a.phone.findPhone('0989309711'))
# a.findPhone('0589309711')
# print(a.phone.getPhones())
# # print(a.phone.getPhone()[0])

# print(a.setPhone('380992261935'))
# print(a.setPhone('0989309711'))
# print(a.setPhone('0989309711'))
# # print(a.getPhone())
# print(a.changePhone('0989309711', '0635656360'))
# print(a.getPhones())

# print(a.showRecord())