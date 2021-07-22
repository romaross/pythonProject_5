#!/usr/bin/python
# -- coding: utf-8 --
# file: task_.py
# date: 20/07/21
'''
3) Два натуральных числа называют дружественными, если каждое из них
равно сумме всех делителей другого, кроме самого этого числа. Найти все
пары дружественных чисел, лежащих в диапазоне от 200 до 300.
'''

from functools import reduce


def get_friendly_nums(max_n, min_n):
    """ Функция - ищет пары дружественных чисел """
    new_dict1 = {}                                                      # Инициализация переменной пустого словаря
    new_set1 = set()                                                    # Инициализация переменной пустого множества
    for n in range(min_n, max_n):                                       # Цикл по диапазону со счётчиком
        friendly_num_or = reduce(lambda a, b: a + b, get_divisors(n))   # Получение суммы делителей счётчика
        if friendly_num_or < min_n or friendly_num_or > max_n:          # Проверка входимости в интервал потель-но ДЧ
            continue                                                    # если нет, то продолжить цикл с начала
        new_dict1[n] = friendly_num_or                                  # ДЧ(друж. числ.) занести в словарь согл. сч.
        if friendly_num_or not in new_set1:                             # Если ДЧ не в множестве
            new_set1.add(n)                                             # , то занести счётчик в множество
        else:                                                           # иначе
            fn2 = reduce(lambda a, b: a + b, get_divisors(friendly_num_or))     # Посчитать сум. дел. друж. числ.
            if fn2 == n:                                                # Если ДЧ равно текущему счётчику
                # 'Friendly numbers: '
                yield n, friendly_num_or    # Передать пару на итерацию вызывающей функции


def get_divisors(x) -> list:
    li1 = [i for i in range(1, x // 2 + 1) if x % i == 0]   # Получение делителей числа x в списке
    return li1                                              # Вернуть список


min_left_n, max_right_n = 200, 300                        # Интервал [min_n ; max_n] для перебора
for a, b in get_friendly_nums(max_right_n, min_left_n):    # Итерация по парам дружественных чисел
    print(a, ' ', b)                            # Вывод пары дружественных чисел
