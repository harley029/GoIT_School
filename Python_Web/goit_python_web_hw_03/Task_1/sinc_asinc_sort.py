"""Sorting files in folders by extension."""

from pathlib import Path
from shutil import copyfile
import sys
from threading import Thread
from time import time
from colorama import Fore


def parse_args():
    """
    Parse command line arguments for the script.
    Returns: tuple: A tuple containing the source and target paths as Path objects.
    Raises: ValueError: If the number of arguments is not 2 or 3.
    """
    if len(sys.argv) == 3:
        source_path = sys.argv[1]
        target_path = sys.argv[2]
    elif len(sys.argv) == 2:
        source_path = sys.argv[1]
        target_path = "dist"
    else:
        print(f"{Fore.RED} [ERROR] {Fore.RESET} Невірна кількість аргументів.")
        sys.exit(1)
    return Path(source_path), Path(target_path)


def folder_list(dir: Path):  # отримує список всіх каталогів (папок)
    """
    Recursively iterate through a directory and append all directories to a list.
    Args: dir (Path): The directory to search.
    Returns: None: The function adds all directories to the global `folders` list.
    """
    for item in dir.iterdir():
        if item.is_dir():
            folders.append(item)
            folder_list(item)


def sort_files(fold: Path, dest: Path):
    """
    Sorts all the files in a given folder by their extension into subfolders in 
    the destination folder.
    Args:
        folder (Path): The path of the folder containing the files to be sorted.
        destination (Path): The path of the destination folder where the sorted 
        files will be placed.
    Returns:
        None: The function sorts the files and places them in the destination folder.
    """
    for file in fold.iterdir():
        if file.is_file():
            extention = file.suffix[1:]
            final_folder = dest.joinpath(extention)
            final_folder.mkdir(exist_ok=True, parents=True)
            copyfile(file, final_folder / file.name)


if __name__ == "__main__":
    # ---------------------- загально-підготовчий режим -------------
    # отримуємо з консолі імена кталогів (вхідний, вихідний)
    sourth, destination = (
        parse_args()
    )
    folders = []  # сторюємо порожній список каталогів (папок)
    folder_list(sourth)  # отримуємо список всіх каталогів (папок)
    folders.append(sourth)  # додаємо до списку папок корневу папку

    # ---------------------- сінхронний режим ----------------------
    timer = time()
    for folder in folders:  # сортуємо файли по папках
        sort_files(folder, destination)
    print(f"Час на виконання в синхронному режимі: {time()-timer} секунд")

    # ---------------------- асінхронний режим ---------------------
    timer = time()
    for folder in folders:
        th = Thread(
            target=sort_files,
            args=(
                folder,
                destination,
            ),
        )
        th.start()
    print(f"Час на виконання в aсинхронному режимі: {time()-timer} секунд")
