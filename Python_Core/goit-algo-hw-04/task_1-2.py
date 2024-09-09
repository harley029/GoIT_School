from pathlib import Path
import re

print('Завдання #1\n')
#-------------------- Task_1 ------------------------------
# Варіант, коли сумми коштів здобуваються з рядку за допомогою регулярного виразу
def total_salary(path:str):
    path_to_file = Path(path)
    if not path_to_file.exists():
        print (f"Такого файлу не існує: {path_to_file}\nПодальше обчислення неможливе.")
        return None, None
    else:
        with open(path_to_file, 'r', encoding="UTF-8") as fh:
            lines = fh.readlines()
        amount=0
        total=0
        pattern=r"\d"
        for line in lines:
            amount +=1
            total += float(''.join(re.findall(pattern, line)))
        average = total / amount
        return total, average

total, average = total_salary("salaries.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

# Варіант, коли сумми коштів здобуваються з рядку під час розбиття його на кортеж з розділом по комі
def total_salary1(path:str):
    path_to_file = Path(path)
    if not path_to_file.exists():
        print (f"Такого файлу не існує: {path_to_file}\nПодальше обчислення неможливе.")
        return None, None
    else:
        with open(path_to_file, 'r', encoding="UTF-8") as fh:
            lines = [el.split(',') for el in fh.readlines()]
        amount=0
        total=0
        for line in lines:
            amount +=1
            total += float(line[1])
        average = total / amount
        return total, average

total, average = total_salary1("salaries.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


input('\nДля переходу до наступного завдання натиснить ENTER\n')
print('Завдання #2\n')
#-------------------- Task_2 ------------------------------
def get_cats_info(path:str):
    path_to_file = Path(path)
    if not path_to_file.exists():
        print (f"Такого файлу не існує: {path_to_file}")
        return None
    else:
        with open(path_to_file, 'r', encoding="UTF-8") as fh:
            lines = [el.split(',') for el in fh.readlines()]
        cat_info=[]
        cat_info_str={}
        for l in lines:
            cat_info_str={"ID":l[0], "name":l[1], "age":l[2].strip()}
            cat_info.append(cat_info_str)
        return cat_info

print(get_cats_info('cats.txt'))
