#!/usr/bin/python
# -- coding: utf-8 --
# file: task_5_2.py
# date: 20/07/21
'''
2) Дано число. Найти сумму и произведение его цифр.
'''


def calc_num_by_digits(_number):
    """ Функция - вычисляет сумму и произведение цифр числа """
    number = str(_number).strip()
    if number.isdigit():  # Условие если число целое
        summa, multi = 0, 1  # Инициализация переменных для суммы и произведения
        for c in number:  # Перебор символов в строке
            digit = int(c)  # Преобразование символа к цифре (0-9)
            summa += digit  # Прибавить цифру к сумме
            multi *= digit  # Умножить цифру на произведение
    else:  # Иначе
        raise Exception('Only integers nums accepted')  # Возбудить исключение с сообщением
    return summa, multi  # Вернуть результаты, сумму и произведение


number = input('Enter a number:')  # Запрос на ввод числа
# print(type(number))
try:  # Обработчик исключения
    (summa, multi) = calc_num_by_digits(number)  # Вызов, вычисление суммы и произведения
    print(f' Summa: {summa} ; Multiplication: {multi}')  # Вывод результатов
except Exception as inst:  # Обработчик исключения
    print(inst)  # Вывод сообщения исключения
