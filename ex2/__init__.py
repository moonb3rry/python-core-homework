from ex2 import fetcher
import time

CALL_COUNT = 10


def benchmark(num):
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов

    :param num: число итераций
    :return: функцию обёртку
    """
    def wrapper(func):
        def decorator(*args, **kwargs):
            totalTime = 0
            for i in range(num):
                start = time.time()
                func(*args, **kwargs)
                end = time.time()
                currentTime = end - start
                totalTime += currentTime
                print(f'Время выполнения: {currentTime}')
            print(f'Среднее время выполнения: {totalTime / num}')
        return decorator
    return wrapper


@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)
