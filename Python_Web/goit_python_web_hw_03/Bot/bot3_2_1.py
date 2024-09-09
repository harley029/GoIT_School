"""
...
"""

from collections import UserList, UserDict
from datetime import datetime
from abc import ABC, abstractmethod

import re
import pickle

from colorama import Fore


# ----- Abstract Classes --------
class AbstractBot(ABC):  # --- реалізація зі строки №287
    """
    ...
    """

    @staticmethod
    @abstractmethod
    def help(filename):
        """
        Opens a file and prints its contents to the console.
        :param filename: The name of the file to open.
        """
        # pass

    @abstractmethod
    def all(self):
        """
        Lists all records in the address book.
        """
        # pass


class AbastractRecord(ABC):
    """
    ...
    """

    @abstractmethod
    def set_name(self, name):
        """
        Sets the name of the record.
        :param name: The new name of the record.
        :return: A message indicating whether the name was set successfully.
        """
        # pass

    @abstractmethod
    def get_name(self):
        """
        Returns the name of the record.
        :return: The name of the record.
        """
        # pass

    @abstractmethod
    def change_name(self, name):
        """
        Changes the name of the record.
        :param name: The new name of the record.
        :return: A message indicating whether the name was changed successfully.
        """
        # pass

    @abstractmethod
    def set_birthday(self, b_day):
        """
        Sets the birthday of the record.
        :param b_day: The new birthday of the record.
        :return: A message indicating whether the birthday was set successfully.
        """
        # pass

    @abstractmethod
    def get_birthday(self):
        """
        Returns the birthday of the record.
        :return: The birthday of the record.
        """
        # pass

    @abstractmethod
    def change_birthday(self, birthday):
        """
        Changes the birthday of the record.
        :param birthday: The new birthday of the record.
        :return: A message indicating whether the birthday was changed successfully.
        """
        # pass

    @abstractmethod
    def set_phone(self, phone):
        """
        Sets the phone number of the record.
        :param phone: The new phone number of the record.
        :return: A message indicating whether the phone number was set successfully.
        """
        # pass

    @abstractmethod
    def change_phone(self, phone1, phone2):
        """
        Changes the phone number of the record.
        :param phone1: The old phone number of the record.
        :param phone2: The new phone number of the record.
        :return: A message indicating whether the phone number was changed successfully.
        """
        # pass

    @abstractmethod
    def del_phone(self, phone):
        """
        Deletes the phone number of the record.
        :param phone: The phone number to delete.
        :return: A message indicating whether the phone number was deleted successfully.
        """
        # pass

    @abstractmethod
    def get_phone(self):
        """
        Returns the phone number of the record.
        :return: The phone number of the record.
        """
        # pass

    @abstractmethod
    def get_phones(self):
        """
        Returns the phone number of the record.
        :return: The phone number of the record.
        """
        # pass

    @abstractmethod
    def find_phone(self, phone):
        """
        Searches for a phone number in the record.
        :param phone: The phone number to search for.
        :return: A message indicating whether the phone number was found in the record.
        """
        # pass

    @abstractmethod
    def find_birthday(self, birthday):
        """
        Searches for a birthday in the record.
        :param birthday: The birthday to search for.
        :return: A message indicating whether the birthday was found in the record.
        """
        # pass

    @abstractmethod
    def show_record(self):
        """
        Returns a string representation of the record.
        :return: A string representation of the record.
        """
        # pass


class Name:
    """
    ...
    """

    def __init__(self, name):
        """
        Initialize a new instance of the Name class.
        Args: name (str): The name of the record.
        """
        self.name = name

    def set_name(self, name):
        """
        Set the name of the record.
        Args: name (str): The new name of the record.
        Returns: str: A message indicating whether the name was set successfully.
        """
        self.name = name
        return (
            f"{Fore.YELLOW}Імʼя {Fore.GREEN}{name}{Fore.YELLOW} встановлено{Fore.RESET}"
        )

    def get_name(self):
        """
        Get the name of the record.
        Returns: str: The name of the record.
        """
        return self.name

    def change_name(self, name):
        """
        Change the name of the record.
        Args: name (str): The new name of the record.
        Returns: str: A message indicating whether the name was changed successfully.
        """
        self.set_name(name)
        return f"{Fore.YELLOW}Імʼя змінено на {Fore.GREEN}{name}{Fore.RESET}"

    def __str__(self) -> str:
        return self.name


class Birthday:
    """
    ...
    """

    def __init__(self):
        """
        Initialize a new instance of the Birthday class.
        """
        self.birthday = datetime

    def set_birthday(self, birthday):
        """
        Set the birthday of the record.
        Args: birthday (str): The new birthday of the record in the format "DD.MM.YYYY".
        Returns: str: A message indicating whether the birthday was set successfully.
        """
        self.birthday = datetime.strptime(birthday, "%d.%m.%Y")
        return (
            f"{Fore.YELLOW}День народження {Fore.GREEN}{birthday} "
            "{Fore.YELLOW}встановлено{Fore.RESET}"
        )

    def get_birthday(self):
        """
        Get the birthday of the record.
        Returns: str: The birthday of the record in the format "DD.MM.YYYY".
        """
        return self.birthday

    def change_birthday(self, birthday):
        """
        Change the birthday of the record.
        Args: birthday (str): The new birthday of the record in the format "DD.MM.YYYY".
        Returns: str: A message indicating whether the birthday was changed successfully.
        """
        self.set_birthday(birthday)
        return f"{Fore.YELLOW}День народження змінено на {Fore.GREEN}{birthday}{Fore.RESET}"

    def find_birthday(self, birthday):
        """
        Check if a birthday matches the record's birthday.
        Args: birthday (str): The birthday to check in the format "DD.MM.YYYY".
        Returns: bool: True if the birthday matches, False otherwise.
        """
        return birthday == self.birthday.strftime("%d.%m.%Y")

    def __str__(self):
        """
        Return the birthday of the record as a string.
        Returns: str: The birthday of the record in the format "DD.MM.YYYY".
        """
        return f"{self.birthday.strftime('%d.%m.%Y')}"


class Phone(UserList):
    """
    ...
    """

    def normalize_pone(self, phone):  # Нормализатор номера телефона
        """
        Normalizes a phone number by adding a leading '+' if it is missing,
        or by adding a '38' prefix if the number is less than 12 digits.
        Args: phone (str): The phone number to normalize
        Returns: str: The normalized phone number
        """
        if len(phone) == 12:
            new_phone = "+" + phone
            return new_phone
        if len(phone) < 12:
            new_phone = "+38" + phone
            return new_phone
        return phone

    def set_phone(self, phone):
        """
        Adds a phone number to the record if it does not already exist.
        Args: phone (str): The phone number to add.
        Returns: str: A message indicating whether the phone number was added or already exists.
        """
        if self.normalize_pone(phone) not in self.data:
            self.data.append(self.normalize_pone(phone))
            return (
                f"{Fore.YELLOW}Номер {Fore.GREEN}{self.normalize_pone(phone)} "
                "{Fore.YELLOW}добавлено.{Fore.RESET}"
            )
        return (
            f"{Fore.RED}Номер {Fore.GREEN}{self.normalize_pone(phone)} "
            "{Fore.RED}вже існує.{Fore.RESET}"
        )

    def get_phone(self):  # возвращает №-ра телефонов списком -> List
        """
        Returns the phone numbers of the record as a list.
        Returns: list: The phone numbers of the record as a list.
        """
        return self.data

    def get_phones(self):  # возвращает №-ра телефонов одной строкой -> Str
        """
        Returns the phone numbers of the record as a string separated by semicolons.
        """
        return f"{'; '.join(self)}"

    def del_phone(self, phone):
        """
        Deletes the phone number of the record.
        Args: phone (str): The phone number to delete.
        Returns: str: A message indicating whether the phone number was deleted successfully.
        """
        self.data.remove(self.normalize_pone(phone))
        return (
            f"{Fore.YELLOW}Номер {Fore.GREEN}{self.normalize_pone(phone)} "
            "{Fore.YELLOW}видалено.{Fore.RESET}"
        )

    def find_phone(self, phone):
        """
        Searches for a phone number in the record.
        Args: phone (str): The phone number to search for.
        Returns: bool: True if the phone number was found in the record, False otherwise.
        """
        return self.normalize_pone(phone) in self.data

    def change_phone(self, phone1, phone2):
        """
        Changes the phone number of the record.
        Args:
            phone1 (str): The old phone number of the record.
            phone2 (str): The new phone number of the record.
        Returns: str: A message indicating whether the phone number was changed successfully.
        """
        self.data.remove(self.normalize_pone(phone1))
        self.set_phone(phone2)
        return (
            f"{Fore.YELLOW}Номер {Fore.GREEN}{self.normalize_pone(phone1)} "
            "{Fore.YELLOW}було змінено на {Fore.GREEN}{self.normalize_pone(phone2)}{Fore.RESET}"
        )


class Record(AbastractRecord):
    """
    ...
    """

    def __init__(self, name):
        """
        Initialize a new instance of the Record class.
        Args: name (str): The name of the record.
        """
        self.name = Name(name)
        self.phone = Phone()
        self.birthday = Birthday()

    def set_name(self, name):
        """
        Set the name of the record.
        Args: name (str): The new name of the record.
        Returns: str: A message indicating whether the name was set successfully.
        """
        self.name = Name(name)
        return (
            f"{Fore.YELLOW}Імʼя {Fore.GREEN}{name} {Fore.YELLOW}встановлено{Fore.RESET}"
        )

    def get_name(self):
        """
        Get the name of the record.
        Returns: str: The name of the record.
        """
        return self.name.get_name()

    def change_name(self, name):
        """
        Change the name of the record.
        Args: name (str): The new name of the record.
        Returns: str: A message indicating whether the name was changed successfully.
        """
        self.name.set_name(name)
        return f"{Fore.YELLOW}Імʼя змінено на {Fore.GREEN}{name}{Fore.RESET}"

    def set_birthday(self, b_day):
        """
        Set the birthday of the record.
        Args: b_day (str): The new birthday of the record in the format "DD.MM.YYYY".
        Returns: str: A message indicating whether the birthday was set successfully.
        """
        return self.birthday.set_birthday(b_day)

    def get_birthday(self):
        """
        Get the birthday of the record.
        Returns: str: The birthday of the record in the format "DD.MM.YYYY".
        """
        return self.birthday.get_birthday()

    def change_birthday(self, birthday):
        """
        Change the birthday of the record.
        Args: birthday (str): The new birthday of the record in the format "DD.MM.YYYY".
        Returns: str: A message indicating whether the birthday was changed successfully.
        """
        self.birthday.set_birthday(birthday)
        return f"{Fore.YELLOW}День народження змінено на {Fore.GREEN}{birthday}{Fore.RESET}"

    def set_phone(self, phone):
        """
        Add a phone number to the record.
        Args: phone (str): The phone number to add.
        Returns: str: A message indicating whether the phone number was added or already exists.
        """
        return self.phone.set_phone(phone)

    def change_phone(self, phone1, phone2):
        """
        Change the phone number of the record.
        Args:
            phone1 (str): The old phone number of the record.
            phone2 (str): The new phone number of the record.
        Returns: str: A message indicating whether the phone number was changed successfully.
        """
        # if self.phone.normalize_pone(phone1) in self.get_phone():
        # 2-й варіант перевірки наявності телефону
        if self.phone.find_phone(phone1):
            return self.phone.change_phone(phone1, phone2)
        return (
            f"{Fore.YELLOW}Tелефонний номер {Fore.GREEN}{self.phone.normalize_pone(phone1)} "
            "{Fore.YELLOW}не знайдерно{Fore.RESET}"
        )

    def del_phone(self, phone):
        """
        Delete a phone number from the record.
        Args: phone (str): The phone number to delete.
        Returns: str: A message indicating whether the phone number was deleted successfully.
        """
        if self.phone.find_phone(phone):
            return self.phone.del_phone(phone)
        return (
            f"{Fore.RED}Tелефонний номер {Fore.GREEN}{self.phone.normalize_pone(phone)} "
            "не знайдерно{Fore.RESET}"
        )

    def get_phone(self):
        """
        Get the phone number of the record.
        Returns: str: The phone number of the record.
        """
        return self.phone.data

    def get_phones(self):
        """
        Get the phone number of the record.
        Returns: str: The phone number of the record.
        """
        return f"{'; '.join(self.phone)}"

    def find_phone(self, phone):
        """
        Check if a phone number exists in the record.
        Args: phone (str): The phone number to check.
        Returns: str: A message indicating whether the phone number was found in the record.
        """
        if self.phone.find_phone(phone):
            return (
                f"{Fore.YELLOW}Номер {Fore.GREEN}{self.phone.normalize_pone(phone)} "
                "{Fore.YELLOW}належить користувачу {Fore.GREEN}{self.get_name()}.{Fore.RESET}"
            )
            # return True
        return (
            f"{Fore.RED}Номер {Fore.GREEN}{self.phone.normalize_pone(phone)} {Fore.RED}"
            "не знайдено.{Fore.RESET}"
        )
        # return False

    def find_birthday(self, birthday):
        """
        Check if a birthday exists in the record.
        Args: birthday (str): The birthday to check.
        Returns: str: A message indicating whether the birthday was found in the record.
        """
        if self.birthday.find_birthday(birthday):
            return (
                f"{Fore.YELLOW}День нарподження {Fore.GREEN}{birthday} {Fore.YELLOW}"
                "належить користувачу {Fore.GREEN}{self.get_name()}{Fore.RESET}"
            )
        return (
            f"{Fore.RED}День нарподження {Fore.GREEN}{birthday} {Fore.RED}"
            "не знайдено{Fore.RESET}"
        )

    def show_record(self):
        """
        Return a string representation of the record.
        Returns: str: A string representation of the record.
        """
        if len(str(self.birthday.get_birthday())) == 19:
            return (
                f"{Fore.GREEN}{self.get_name()}{Fore.RESET}; тел.: {self.phone.get_phones()}, "
                "д.н.: {self.birthday.get_birthday().strftime('%d.%m.%Y')}."
            )
        return f"{Fore.GREEN}{self.get_name()}{Fore.RESET}; тел.: {self.phone.get_phones()}."

    def __str__(self):
        """
        Return a string of the record.
        """
        if len(str(self.birthday.get_birthday())) == 19:
            return (
                f"{self.get_name()}; {self.phone.get_phones()}; "
                "{self.birthday.get_birthday().strftime('%d.%m.%Y')}"
            )
        return f"{self.get_name()}; {self.phone.get_phones()}"


class AddressBook(UserDict):
    """
    Main subclass
    """

    def add_record(self, record):
        """
        Adds a new record to the address book.
        Args: record (AddressBook): The record to add.
        Returns: str: A message indicating whether the record was added successfully.
        """
        self.data[record] = record
        return (
            f"{Fore.YELLOW}Запис {Fore.GREEN}{record.get_name()} "
            "{Fore.YELLOW}доданий до адресної книги.{Fore.RESET}"
        )

    def print_book(self):
        """
        Prints the contents of the address book in a readable format.
        """
        munb = 1
        for rec in self.data:
            if len(str(self.data[rec].get_birthday())) == 19:
                print(
                    f"{munb:3}. {self.data[rec].get_name():12} тел. {self.data[rec].get_phones()}"
                )
                print(
                    f"{' ':17} д.н. {self.data[rec].get_birthday().strftime('%d.%m.%Y')}"
                )
                munb += 1
            else:
                print(
                    f"{munb:3}. {self.data[rec].get_name():12} тел. {self.data[rec].get_phones()}"
                )
                munb += 1

    def select(self, name):
        """
        Searches for a record in the address book based on the name.
        Args: name (str): The name of the record to search for.
        Returns: AddressBook: The record if found, None otherwise.
        """
        for n in self.data:
            if self.data[n].get_name() == name:  # Запис знайдено
                return self.data[n]

    def if_exist(self, name):
        """
        Check if a record with a given name exists in the address book.
        Args: name (str): The name of the record to check.
        Returns: bool: True if a record with the given name exists, False otherwise.
        """
        found = False
        for n in self.data:
            if self.data[n].get_name() == name:
                found = True
        return found

    def delete(self, name):
        """
        Delete a record from the address book.
        Args: name (str): The name of the record to delete.
        Returns: AddressBook: The updated address book.
        Raises: ValueError: If the record does not exist in the address book.
        """
        if self.if_exist(name):
            temp_book = AddressBook()
            for n in self.data:
                if not str(self.data[n].get_name()) == name:
                    temp_book[n] = self.data[n]
            print(
                f"{Fore.YELLOW}Запис {Fore.GREEN}{name} {Fore.YELLOW}видалено.{Fore.RESET}"
            )
            return temp_book
        print(f"{Fore.RED}Запис {Fore.GREEN}{name} {Fore.RED}не знайдено.{Fore.RESET}")
        return self

    def find_phone(self, phone):
        """
        Searches for a phone number in the record.
        Args: phone (str): The phone number to search for.
        Returns: bool: True if the phone number was found in the record, False otherwise.
        """
        for rec in self.data:
            if self.data[rec].phone.find_phone(phone):
                return self.data[rec].find_phone(phone)
        return f"Номер {phone} відсутній"
        # print(self.data[rec].phone.find_phone(phone))

    def find_birthday(self, birthday):  # ++ добавити перевірку формату
        """
        Searches for a birthday in the record.
        Args: birthday (str): The birthday to search for.
        Returns: str: A message indicating whether the birthday was found in the record.
        """
        for rec in self.data:
            if len(str(self.data[rec].get_birthday())) == 19:
                if self.data[rec].birthday.find_birthday(birthday):
                    return self.data[rec].find_birthday(birthday)
        return f"{Fore.RED}День народження {Fore.GREEN}{birthday} {Fore.RED}відсутній.{Fore.RESET}"


class SimpleBot(AbstractBot):
    """
    Simple Bot for the Help and All.
    """

    def __init__(self, book: AddressBook):
        """
        Initialize the SimpleBot class.
        Args: book (AddressBook): The address book to use.
        """
        self.data = book

    @staticmethod
    def help(filename):
        """
        Open and print the contents of a help file.
        Args: filename (str): The name of the file to open.
        """
        with open(filename, "r", encoding="UTF-8") as fh:
            print(fh.read())

    def all(self):
        """
        Print all records in the address book.
        """
        self.data.print_book()


# ================================ Функції логики боту ==================================#
def parse_input(user_input):
    """
    Parse a user input string into a command and arguments.
    Args: user_input (str): The input string from the user.
    Returns: tuple: A tuple containing the command and arguments.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


# ------- додає Запис до Адресної книги
def add_to_book(args, record: AddressBook):
    """
    Add a new record to the address book.
    Args:
        args (list): The arguments of the command.
        record (AddressBook): The address book to add the record to.
    Returns:  AddressBook: The updated address book.
    """
    record = record.add_record(args)
    return record


# ------- видає список днів народження з Адресної книги, які відбудуться протягом 7 днів
def get_upcomming_birthdays(users):
    """
    Get a list of upcoming birthdays from the address book.
    Args: users (dict): The records in the address book.
    Returns: list: A list of upcoming birthdays.
    """
    today = datetime.today()
    birthday_list = []
    for user in users:
        if len(str(users[user].get_birthday())) == 19:
            tempt_b_day = datetime(
                year=today.year,
                month=user.get_birthday().month,
                day=user.get_birthday().day,
            )
            diffr_days = tempt_b_day.toordinal() - today.toordinal()
            if 0 <= diffr_days < 7:
                birthday_list.append(
                    {
                        "name": user.get_name(),
                        "birthday": tempt_b_day.strftime("%d.%m.%Y"),
                    }
                )
    if birthday_list:
        print(f"{Fore.YELLOW}Список найближчих іменинників:{Fore.RESET}")
        # lambda x: x in birthday_list, (map((print(birthday_list[x]['name'], ' - ',
        # birthday_list[x]['birthday'])), birthday_list))
        for i in birthday_list:
            print(f"{Fore.GREEN}{i['name']}{Fore.RESET} - {i['birthday']}")
        return birthday_list
    print("Найближчими днями іменинників - немає")
    return birthday_list


# ------- виводить справку по командам
# def help(file):
#     with open(file, 'r', encoding="UTF-8") as fh:
#         print(fh.read())


# ------- видаляє Запис з Адресної книги
def delrec(name, book):
    """
    Delete a record from the address book.
    Args:
        name (str): The name of the record to delete.
        book (AddressBook): The address book to delete the record from.
    Returns: AddressBook: The updated address book.
    """
    book = book.delete(name)
    return book


# ------- додає нову Запис до Адресної книги в залежності від кількості аргументів (імʼя, тел., д/p)
def create_record(args, book):  # додати перевірку формату тел и др
    """
    Create a new record in the address book.
    Args:
        args (list): The arguments of the command.
        book (AddressBook): The address book to add the record to.
    """
    if len(args) == 1:
        args[0] = Record(args[0])
        add_to_book(args[0], book)
    if len(args) == 2:
        args[0] = Record(args[0])
        args[0].set_phone(args[1])
        add_to_book(args[0], book)
    if len(args) == 3:
        args[0] = Record(args[0])
        args[0].set_phone(args[1])
        args[0].set_birthday(args[2])
        add_to_book(args[0], book)


# ------- перевірка чи строка є телефонним номером
def is_ph_number(number: str) -> bool:
    """
    Check if a string is a valid phone number.
    Args: number (str): The phone number to check.
    Returns: bool: True if the number is valid, False otherwise.
    """
    if number.isdigit() and (10 <= len(number) <= 12):
        return True
    return False


# ------- перевірка чи строка є датою
def is_date(date: str) -> bool:
    """
    Check if a string is a valid date.
    Args: date (str): The date to check.
    Returns: bool: True if the date is valid, False otherwise.
    """
    # date=''.join(re.findall(r"\d{2}\.\d{2}\.\d{4}", date))
    if "".join(re.findall(r"\d{2}\.\d{2}\.\d{4}", date)):
        return True
    return False


# ------- виводить імʼя активного запису під час його редагування (під час вводу команд).
def rec_mode(rec, book):
    """
    Enter record editing mode.
    Args:
        rec (str): The name of the record to edit.
        book (AddressBook): The address book to use.
    """

    def rec_mode_name(name):
        return f"[ {Fore.GREEN}{name.get_name()}{Fore.RESET} ] >>> "

    print(f"{Fore.GREEN}Режим редагування запису!{Fore.RESET}\n")
    name = book.select(rec)  # тимчасовий запис для редагування
    while True:
        user_input = input(rec_mode_name(name))
        command, *args = parse_input(user_input)
        if command == "quit":
            return book
        if command == "change_name" and len(args) == 1:
            print(name.set_name(args[0]))
        elif command == "set_phone" and len(args) == 1 and is_ph_number(args[0]):
            print(name.set_phone(args[0]))
        elif (
            command == "change_phone"
            and len(args) == 2
            and is_ph_number(args[0])
            and is_ph_number(args[1])
        ):
            print(name.change_phone(args[0], args[1]))
        elif command == "delete_phone" and len(args) == 1 and is_ph_number(args[0]):
            print(name.del_phone(args[0]))
        elif command == "set_birthday" and len(args) == 1 and is_date(args[0]):
            print(name.set_birthday(args[0]))
        elif command == "print":
            print(name.show_record())
        elif command == "help":
            SimpleBot.help("help_rec_mode.txt")
        else:
            print(warning())
    return book


# ------- виводить повідомлення про помилку
def warning():
    """
    Returns a warning message indicating that the command or arguments are incorrect.
    The message includes instructions on how to access help.
    """
    return (
        f"{Fore.RED}Error:{Fore.RESET} Невірна команда або аргумент(-ти)\n{' ':7}"
        "Для довідки - введить {Fore.GREEN}help{Fore.RESET}\n"
    )


# ------- серіалізує книгу у файл
def save_data(book, filename="addressbook.pkl"):
    """
    Save the address book data to a file.
    Args:
        book (AddressBook): The address book to save.
        filename (str, optional): The name of the file to save to. Defaults to "addressbook.pkl".
    Returns: None
    """
    with open(filename, "wb") as file:
        pickle.dump(book, file)


# ------- десеріалізує книгу з файлу
def load_data(filename="addressbook.pkl"):
    """Loads the data from the specified file.
    Args: filename (str, optional): The name of the file to load. Defaults to "addressbook.pkl".
    Returns:  AddressBook: The loaded data.
    Raises: FileNotFoundError: If the file cannot be found.
    """
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return AddressBook()  # Повернення нової адресної книги, якщо файл не знайдено


def main():
    """
    Main function of the application.
    """
    book = load_data()  # Завантаження збереженої книги
    client_bot = SimpleBot(book)

    print(f"{Fore.GREEN}Welcome to the assistant bot!{Fore.RESET}")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit", "quit"]:
            print(f"{Fore.GREEN}Good bye!{Fore.RESET}")
            save_data(book)
            break
        if command == "hello":
            print("How can I help you?\n(type HELP for the list of commands)")
        elif command == "delete":
            if args:
                book = book.delete(args[0])
            else:
                print("Не введено імʼя.")
            # delrec(args[0], book)
        elif command == "all":
            client_bot.all()
        elif command == "birthdays":
            get_upcomming_birthdays(book)
        elif command == "help":
            client_bot.help("help.txt")
        elif command == "change_name" and len(args) == 2:
            print(book.select(args[0]).change_name(args[1]))
        elif (
            command == "change_phone"
            and len(args) == 3
            and is_ph_number(args[1])
            and is_ph_number(args[2])
        ):
            print(book.select(args[0]).change_phone(args[1], args[2]))
        elif command == "find_phone" and len(args) == 1 and is_ph_number(args[0]):
            print(book.find_phone(args[0]))
        elif command == "delete_phone" and len(args) == 2 and is_ph_number(args[1]):
            print(book.select(args[0]).del_phone(args[1]))
        elif command == "set_phone" and len(args) == 2 and is_ph_number(args[1]):
            print(book.select(args[0]).set_phone(args[1]))
        elif command == "print" and len(args) == 1:
            if book.if_exist(args[0]):
                print(book.select(args[0]).show_record())
            else:
                print(f"Запис {args[0]} не знайдено.")
        elif command == "add" and len(args) >= 1:
            print(create_record(args, book))
        elif command == "find_birthday" and len(args) == 1 and is_date(args[0]):
            print(book.find_birthday(args[0]))
        elif command == "change_birthday" and len(args) == 2 and is_date(args[1]):
            print(book.select(args[0]).birthday.change_birthday(args[1]))
        elif command == "set_birthday" and len(args) == 2 and is_date(args[1]):
            print(book.select(args[0]).set_birthday(args[1]))
        elif command == "record_mode" and len(args) == 1:
            if book.select(args[0]):
                rec_mode(args[0], book)
            else:
                print(f"Імʼя {args[0]} не знайдено.")
        else:
            print(warning())


if __name__ == "__main__":
    main()
