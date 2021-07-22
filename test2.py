import datetime as dt
from random import randint as rnd


def running_time(func):
    ret_val = None

    def func2():
        nonlocal ret_val
        return ret_val

    def wrapper():
        nonlocal ret_val
        start = dt.datetime.now()
        ret_val = func()
        finish = dt.datetime.now()
        run_time = finish - start
        print('Оборачиваемая функция  {} время выполнения {}'.format(func.__name__, run_time))
        return func2

    return wrapper()


@running_time
def main_func():
    """ Test function """
    print(' A long long circle..')
    for _ in range(rnd(1e7, 1e8)):
        continue
    return [1, 2, 3]


print(' main result ', main_func())