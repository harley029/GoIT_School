from pathlib import Path
import re
import sys

def generator_numbers(line:str):
    pattern=r"\d+\.\d+"
    yield ''.join(re.findall(pattern, line))
    
def sum_profit(lines:str, func:callable):
    lines=lines.split(' ')
    sum=0
    for line in lines:
        res=next(func(line))
        if res:
            sum +=float(res)
    return sum

def main():
    # отримуємо текст із файлу text.txt, переданого як аргумент
    if len(sys.argv) > 1:
        path_to_file = Path(sys.argv[1])
        with open(path_to_file, 'r', encoding="UTF-8") as fh:
            lines = fh.readline().strip()
    # -----------------------------------------------------------
    # виконуємо оробку отриманого тексту
        total_income = sum_profit(lines, generator_numbers)
        print(f"Загальний дохід: {total_income}")
    # -----------------------------------------------------------
    else:
        print(f"Не указано имя файлу.")
    
if __name__ == "__main__":
    main()

# параметри виклику скрипту: python3 task_2.py text.txt