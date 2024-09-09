from time import time
from multiprocessing import Process, Semaphore, Manager, cpu_count
import sys


def factorize_sinc_mode(*number) -> list:
    out_list = []
    for item in number:
        item_list = []
        for i in range(1, item + 1):
            if item % i == 0:
                item_list.append(i)
        out_list.append(item_list)
    return out_list


def factorize(semaphore: Semaphore, number: int, rezult: list) -> list:
    with semaphore:
        out_list = []
        for i in range(1, number + 1):
            if number % i == 0:
                out_list.append(i)
        # print(out_list)  # роздруківка поточного списку (для контроля)
        rezult.append(out_list)
        sys.exit(0)


def factorize_asinc_mode(*number) -> list:
    semaphore = Semaphore(cpu_count() - int(len(number)))
    fin_lst = []
    with Manager() as manager:
        rezult = manager.list()
        process = []
        for item in number:
            pr = Process(target=factorize, args=(semaphore, item, rezult,),)
            pr.start()
            process.append(pr)
        [pr.join() for pr in process]
        # print(rezult) # друкує нормальний лист, але він не передається через return. Чому?
        for item in rezult:
            fin_lst.append(item)
    return fin_lst


if __name__ == "__main__":
    # ------------------------- сінхронний режим -------------------------
    start = time()
    a, b, c, d = factorize_sinc_mode(128, 255, 99999, 10651060)
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    print(f"Час на виконання в синхронному режимі: {time()-start} секунд")

    # ------------------------- асинхронний режим -------------------------
    start = time()
    a, b, c, d = factorize_asinc_mode(128, 255, 99999, 10651060)
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    print(f"Час на виконання в aсинхронному режимі: {time()-start} секунд")
