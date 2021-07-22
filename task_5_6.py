from random import randint


def main_func():
    """ Test function """
    numbers = [randint(1, 99) for _ in range(19)]   # Генерация списка из 19 элементов со случайными числами от[1;99]
    print(numbers)                                  # Вывод списка
    count = count_growing_intervals(numbers)        # Вызов функции подсчёта
    print(' Count of growing intervals:', count)    # Вывод результата


def count_growing_intervals(numbers):
    """ Функция - подсчёт возрастающих интервалов """
    numbers.append(0)                       # Добавить ноль в конец списка
    count = 0                               # Инициализация результата нулём
    least_one = False                       # Инициализация булевой переменной = ложь
    for ix in range(1, len(numbers)):       # Цикл со счётчиком по списку (со второго элемента)
        if numbers[ix] > numbers[ix - 1]:   # Если текущий элем. больше предыдущ. то последов. возрастает
            least_one = True                # Есть раст. посл. = истин.
            continue                        # Продолжить цикл с начала ( счётчик следующий)
        else:                               # Иначе, последовательность уже не возрастает
            if least_one:                   # но последовательность уже имела возрастающий интервал
                least_one = False           # Сброс булевой переменной
                count += 1                  # Плюс один к ответу
                print('Index', ix)          # Тест - вывод индекса
    numbers.pop(len(numbers)-1)             # Убрать ноль с конца списка
    return count                            # Вернуть ответ


if __name__ == '__main__':
    main_func()
