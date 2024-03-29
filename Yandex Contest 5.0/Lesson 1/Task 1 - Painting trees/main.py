# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
#
# Вася и Маша участвуют в субботнике и красят стволы деревьев в белый цвет. Деревья растут вдоль улицы через равные
# промежутки в 1 метр. Одно из деревьев обозначено числом ноль, деревья по одну сторону занумерованы
# положительными числами 1, 2 и т.д., а в другую — отрицательными −1,−2 и т.д.
# Ведро с краской для Васи установили возле дерева P, а для Маши — возле дерева Q. Ведра с краской очень тяжелые и
# Вася с Машей не могут их переставить, поэтому они окунают кисть в ведро и уже с этой кистью идут красить дерево.
# Краска на кисти из ведра Васи засыхает, когда он удаляется от ведра более чем на V метров,
# а из ведра Маши — на M метров. Определите, сколько деревьев может быть покрашено.
#
# Формат ввода
# В первой строке содержится два целых числа P и V — номер дерева, у которого стоит ведро Васи
# и на сколько деревьев он может от него удаляться. Во второй строке содержится два целых числа
# Q и M — аналогичные данные для Маши. Все числа целые и по модулю не превосходят 10 ** 8.
#
# Формат вывода
# Выведите одно число — количество деревьев, которые могут быть покрашены.
#
# Пример
# Ввод
# 0 7
# 12 5
#
# Вывод
# 25

with open('input.txt', 'r', encoding='utf-8') as file:
    p, v, q, m = map(int, file.read().split())
    left1 = p - v
    right1 = p + v

    left2 = q - m
    right2 = q + m

    if right2 < left1 or right1 < left2:
        print((2 * v + 1) + (2 * m + 1))
    else:
        print(abs(min(left1, left2)) + abs(max(right1, right2)) + 1)
