#"''Создать список из 20 целых случайных чисел в диапазоне от -20
#до 20. Используя функцию filter, отобрать из списка числа,
#которые больше либо равны среднему арифметическому всех
#чисел из исходного списка

from random import randint
numbers = [randint(-20, 20) for i in range(20)]
print(numbers)
avg = sum(numbers) / 20
print(avg)
b = list(filter(lambda x:x >= avg, numbers))
print(b)