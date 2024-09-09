from pathlib import Path
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

# функція виводу резулльтатів підрахунків
def display_log_counts(counts: dict):
    print(f"Рівень логування | Кількість")
    print(f"-----------------|-----------")
    print(f"INFO             | {counts['INFO']}")
    print(f"DEBUG            | {counts['DEBUG']}")
    print(f"ERROR            | {counts['ERROR']}")
    print(f"WARNING          | {counts['WARNING']} \n")
    
# функція сортування повідомлень за темою
def filter_logs_by_level(logs: list, level: str):
    print(f"Деталі логів для рівня '{level}':")
    for i in range(len(logs)):
        if logs[i]['level'] == 'INFO' and level == 'INFO':
            print(f"{logs[i]['data']} {logs[i]['time']} - {logs[i]['message']}")
        if logs[i]['level'] == 'DBUG' and level == 'DEBUG':
            print(f"{logs[i]['data']} {logs[i]['time']} - {logs[i]['message']}")    
        if logs[i]['level'] == 'ERROR' and level == 'ERROR':
            print(f"{logs[i]['data']} {logs[i]['time']} - {logs[i]['message']}")
        if logs[i]['level'] == 'WARNING' and level == 'WARNING':
            print(f"{logs[i]['data']} {logs[i]['time']} - {logs[i]['message']}")

def main():
    try:
        if len(sys.argv) > 1:                  # перевірка наявності аргумента с именем файла
            path_to_file = Path(sys.argv[1])
        log=load_logs(path_to_file)            # завантаження логу з парсингом
        numb_mist=count_logs_by_level(log)     # підрахунок повідомлень за типами
        display_log_counts(numb_mist)          # вивід результатів підрахунку
        try:                                   # вивід повідомлень відповідно до теми
            if sys.argv[2]:
                filter_logs_by_level(log, str(sys.argv[2]))   
        except IndexError:
            pass
    except UnboundLocalError:
        print("Не введено ім'я LOG - файлу")

if __name__ == "__main__":
    main()