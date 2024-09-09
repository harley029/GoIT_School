from time import time
from multiprocessing import Pool, cpu_count

# -----------------------логіка сінхронного режиму -------------------------
def factorize_sinc_mode(*number) -> list:
    out_list = []
    for item in number:
        item_list = []
        for i in range(1, item + 1):
            if item % i == 0:
                item_list.append(i)
        out_list.append(item_list)
    return out_list

# -----------------------логіка асінхронного режиму -------------------------
def factorize(number: int) -> list:
    out_list = []
    for i in range(1, number + 1):
        if number % i == 0:
            out_list.append(i)
    return out_list

def factorize_asinc_mode(*number) -> list:
    with Pool(cpu_count()) as pool:
        r=pool.map(factorize, number)
    return r


def factorize_async_batch(numbers, batch_size):
    with Pool(cpu_count()) as pool:
        results = []
        for i in range(0, len(numbers), batch_size):
            batch = numbers[i : i + batch_size]
            batch_results = pool.map(factorize, batch)
            results.extend(batch_results)
    return results


if __name__ == "__main__":
    # ------------------------- сінхронний режим -------------------------
    start = time()
    a, b, c, d = factorize_sinc_mode(128, 255, 99999, 10651060)
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553,
                 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    print(f"Час на виконання в синхронному режимі:\t\t {time()-start:f} секунд")

    # ------------------------- асинхронний режим -------------------------
    start = time()
    a, b, c, d = factorize_asinc_mode(128, 255, 99999, 10651060)
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553,
                 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    print(f"Час на виконання в aсинхронному режимі:\t\t {time()-start:f} секунд")

    # ------------------------- асинхронний batch-режим -------------------------
    start = time()
    a, b, c, d = factorize_async_batch([128, 255, 99999, 10651060], 2)
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553,
                 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    print(f"Час на виконання в aсинхронному batch- режимі:\t {time()-start:f} секунд")
