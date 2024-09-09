from pathlib import Path, PurePath
from colorama import Fore
import sys

def list_dir(path_name:str):
    directory = Path(path_name)
    for path in directory.iterdir():
        p=PurePath(path)
        if path.is_dir():
            print(f"{Fore.GREEN}{p.parent}/")
            list_dir(path)
        else:
            print(f"{Fore.GREEN}{p.parent}/{Fore.BLUE}{p.name}")

def main():
    if len(sys.argv) > 1:
        list_dir(sys.argv[1])
    else:
        print(f"{Fore.RED} [ERROR] {Fore.RESET} Не указано имя каталогу.")

if __name__ == "__main__":
    main()
