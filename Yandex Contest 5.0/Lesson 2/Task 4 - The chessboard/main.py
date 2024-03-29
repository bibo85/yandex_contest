# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
#
# Из шахматной доски по границам клеток выпилили связную (не распадающуюся на части) фигуру без дыр.
# Требуется определить ее периметр.
#
# Формат ввода
# Сначала вводится число N (1 ≤ N ≤ 64) – количество выпиленных клеток.
# В следующих N строках вводятся координаты выпиленных клеток, разделенные пробелом
# (номер строки и столбца – числа от 1 до 8). Каждая выпиленная клетка указывается один раз.
#
# Формат вывода
# Выведите одно число – периметр выпиленной фигуры (сторона клетки равна единице).

# Пример 1
# Ввод
# 3
# 1 1
# 1 2
# 2 1
#
# Вывод
# 8

# Пример 2
# Ввод
# 1
# 8 8
#
# Вывод
# 4

from collections import deque


def get_perimeter(coors):
    if len(coors) == 1:
        return 4
    if len(coors) == 2:
        return 6

    result = 0

    # создаем очередь для проверки
    q = deque()
    for coor in coors:
        q.append((coor[0], coor[1]))

    while q:
        x, y = q.pop()  # Берем элементы с конца очереди
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # 4-е направления для проверки
        counter = 4
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # Если координата в поле и она есть в нашем списке координат,
            # то убираем эту сторону из периметра.
            if nx in range(1, 9) and ny in range(1, 9) and [nx, ny] in coors:
                counter -= 1
        result += counter

    return result


with open('input.txt', 'r', encoding='utf-8') as file:
    coors_cnt = int(file.readline())
    coors = []
    for _ in range(coors_cnt):
        coors.append(list(map(int, file.readline().split())))
    ans = get_perimeter(coors)
    print(ans)

# Tests
# tests = [
#     (3, [[1, 1], [1, 2], [2, 1]], 8),
#     (1, [[8, 8]], 4),
#     (2, [[8, 8], [8, 7]], 6),
#     (4, [[1, 1], [1, 2], [1, 3], [2, 1]], 10),
#     (5, [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2]], 10),
#     (5, [[1, 1], [1, 2], [1, 3], [2, 2], [2, 3]], 10),
#     (6, [[1, 1], [1, 2], [1, 3], [2, 2], [3, 2], [3, 3]], 14),
#     (3, [[3, 1], [3, 2], [3, 3]], 8),
#     (4, [[3, 1], [3, 2], [3, 3], [2, 3]], 10),
#     (5, [[3, 1], [3, 2], [3, 3], [2, 3], [2, 2]], 10),
#     (3, [[1, 3], [2, 3], [3, 3]], 8),
#     (6, [[2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]], 10),
# ]
#
# for coor_cnt, i_coors, ans in tests:
#     assert get_coor(i_coors) == ans, f'Тест {coor_cnt, i_coors, ans}'
