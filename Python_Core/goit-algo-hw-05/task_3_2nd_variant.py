from pathlib import Path
import sys, re

# функція считування файлу по строкам з послідуючим парсингом, створює лист зі словников
def load_logs(file_path: str) -> list:
    with open(file_path, 'r', encoding="UTF-8") as fh:
        parsed_log=list(filter(lambda x: x is not None, map(parse_log_line, fh.readlines()))) # map заменяет цикл for при чтении файла по строкам
    return parsed_log

# функція парсингу вхідной строки, створює словник
def parse_log_line(string: str):
    
    if not re.match(r"\d{4}\-\d{2}\-\d{2} \d{2}\:\d{2}\:\d{2} (\w+) (.*)", string):
        return None
    date, time, level, *message = string.split(' ')
    return {'date':date, 'time':time, 'level':level, 'message':' '.join(message)}
    
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
    return list(filter(lambda x: x['level'] == level, logs))

def main():
    try:
        if len(sys.argv) > 1:                  # перевірка наявності аргумента с именем файла
            path_to_file = Path(sys.argv[1])
        log=load_logs(path_to_file)            # завантаження логу з парсингом
        numb_mist=count_logs_by_level(log)     # підрахунок повідомлень за типами
        display_log_counts(numb_mist)          # вивід результатів підрахунку
        try:                                   # вивід повідомлень відповідно до теми
            if sys.argv[2]:
                logs=filter_logs_by_level(log, sys.argv[2])
                print(f"Деталі логів для рівня '{sys.argv[2]}':")
                print(''.join(map(lambda x:f"{x['date']} {x['time']} - {x['message']}", logs)))  
        except IndexError:
            pass
    except UnboundLocalError:
        print("Не введено ім'я LOG - файлу")

if __name__ == "__main__":
    main()