from pathlib import Path
from collections import Counter
import sys, re

# функція считування файлу по строкам з послідуючим парсингом
# створює лист зі словников
def load_logs(file_path: str):
    parsed_log=list()
    with open(file_path, 'r', encoding="UTF-8") as fh:
        for line in fh:
            parsed_log.append(parse_log_line(line))
    return parsed_log

# функція парсингу вхідной строки, створює словник
def parse_log_line(string: str):
    # сплітуємо строку по символу ПРОБІЛ та створюємо тимчасрві змінні
    lines=string.strip().split(' ')
    ls=[]
    s=''
    # виборка значень ДАТА, ВРЕМЯ, РІВЕНЬ в окремий список
    for line in lines:
        date=''.join(re.findall(r"\d{4}\-\d{2}\-\d{2}", line))
        if date:
            ls.append(date)
        time=''.join(re.findall(r"\d{2}\:\d{2}\:\d{2}", line))
        if time:
            ls.append(time)
        level=''.join(re.findall(r"INFO", line)) or ''.join(re.findall(r"ERROR", line)) or ''.join(re.findall(r"DEBUG", line)) or ''.join(re.findall(r"WARNING", line))
        if level:
            ls.append(level)
    # видалення значень ДАТА, ВРЕМЯ, РІВЕНЬ з вхідного списку
    lines.remove(ls[0])
    lines.remove(ls[1])
    lines.remove(ls[2])
    # збірка значення MESSAGE та його додавання до окремого списку
    for x in range(len(lines)):
         s=s+lines[x]+' '
    ls.append(s.strip())
    log={'data':ls[0], 'time':ls[1], 'level':ls[2], 'message':ls[3]}
    return log

# функція підрахунку повідомлень за темою, створює словник
def count_logs_by_level(logs:list):
    number_of_messages={'INFO':0, 'ERROR':0, 'DEBUG':0, 'WARNING':0}
    for i in range(len(logs)):
        if logs[i]['level'] == 'INFO':
            number_of_messages['INFO'] +=1
        if logs[i]['level'] == 'DEBUG':
            number_of_messages['DEBUG'] +=1
        if logs[i]['level'] == 'ERROR':
            number_of_messages['ERROR'] +=1
        if logs[i]['level'] == 'WARNING':
            number_of_messages['WARNING'] +=1
        # print(logs[i]['level'])
    return number_of_messages

# функція сортування повідомлень за темою
def filter_logs_by_level(logs: list, level: str):
    for i in range(len(logs)):
        if logs[i]['level'] and level == 'INFO':
            print(logs[i])

def main():
    log=load_logs('log.log') # завантаження логу з парсингом
    numb_mist=count_logs_by_level(log) #підрахунок повідомлень за типами
    filter_logs_by_level

if __name__ == "__main__":
    main()