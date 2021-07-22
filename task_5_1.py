def main_func():
    """ Test function """
    symbol = ''                                                 # Пустая строка для выражения
    while symbol != '0':                                        # Цикл пока не введён нулевой символ
        symbol = input('Prompt , expression (X [+|-|*|/] Y):')  # Запрос для ввода выражения
        try:                                                    # Обработчик исключения
            print('Z=', eval(symbol))                           # Вывод вычисленного выражения ( встроенная функция)
        except ZeroDivisionError:                               # Обработка деления на ноль
            print('Can not divide by zero!')                    # Диагностическое сообщение
        except SyntaxError:                                     # Обработка синтасических ошибок в выражении
            print('Invalid expression:')                        # Диагностическое сообщение


if __name__ == '__main__':
    main_func()