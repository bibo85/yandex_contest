# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
#
# Вася играет в настольную игру «Пираты Баренцева моря», которая посвящена морским битвам.
# Игровое поле представляет собой квадрат из N×N клеток, на котором расположено N кораблей
# (каждый корабль занимает одну клетку).
# Вася решил воспользоваться линейной тактикой, для этого ему необходимо выстроить все N кораблей в одном столбце.
# За один ход можно передвинуть один корабль в одну из четырёх соседних по стороне клеток.
# Номер столбца, в котором будут выстроены корабли, не важен. Определите минимальное количество ходов,
# необходимых для построения кораблей в одном столбце.
# В начале и процессе игры никакие два корабля не могут находиться в одной клетке.
#
# Формат ввода
# В первой строке входных данных задаётся число N (1≤N≤100). В каждой из следующих N строк задаются координаты корабля:
# сначала номер строки, затем номер столбца (нумерация начинается с единицы).
#
# Формат вывода
# Выведите одно число — минимальное количество ходов, необходимое для построения.
#
# Пример
# Ввод
# 3
# 1 2
# 3 3
# 1 1
#
# Вывод
# 3


def count_steps(num_cnt, coors_lst, i_col, ship_in_rows):
    row_without_ship = []  # строки без кораблей
    row_with_many_ships = []  # строки с количеством кораблей больше 1

    for i in range(num_cnt):
        if ship_in_rows[i] == 0:
            row_without_ship.append(i)
        if ship_in_rows[i] > 1:
            row_with_many_ships.extend([i] * (ship_in_rows[i] - 1))

    # находим количество сдвигов по горизонтали  к i_col колонке
    shift_col = 0
    for coor in coors_lst:
        shift_col += abs(coor[1] - 1 - i_col)

    # находим количество сдвигов по вертикали
    # От строк с большим количеством кораблей к строкам где кораблей вообще нет
    shift_row = 0
    for i in range(len(row_without_ship)):
        shift_row += abs(row_without_ship[i] - row_with_many_ships[i])

    return shift_col + shift_row


def steps_count(coors_cnt, coors):
    # создаем список с количеством кораблей на каждой строке с изначально нулевым количеством кораблей
    ship_count_in_rows = [0] * coors_cnt

    # пробегаем по всем координатам и собираем количество кораблей в строках
    for i in range(coors_cnt):
        # получаем строку, в которой стоит корабль
        row = coors[i][0]
        # добавляем корабль в список в нужной строке
        ship_count_in_rows[row - 1] += 1

    # подсчитываем количество необходимых шагов в зависимости от колонки, где будем собирать корабли
    results = []
    for i_col in range(coors_cnt):
        res = count_steps(coors_cnt, coors, i_col, ship_count_in_rows)
        results.append(res)

    # возвращаем минимально возможное количество шагов
    return min(results)


with open('input.txt', 'r', encoding='utf-8') as file:
    count = int(file.readline())
    coors = []
    for _ in range(count):
        coors.append(list(map(int, file.readline().split())))
    ans = steps_count(count, coors)
    print(ans)

# Tests
# tests = [
#     (3, [[1, 2], [3, 3], [1, 1]], 3),
#     (3, [[1, 1], [1, 2], [3, 3]], 3),
#     (5, [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], 6),
#     (3, [[2, 1], [2, 2], [2, 3]], 4),
#     (10, [[1, 6], [6, 2], [5, 5], [7, 5], [8, 9], [6, 10], [8, 2], [10, 8], [8, 7], [7, 8],], 35),
#     (10, [[9, 4], [8, 9], [5, 4], [10, 8], [7, 9], [10, 5], [9, 2], [8, 10], [3, 9], [6, 2],], 48),
#     (20, [[13, 19], [3, 13], [20, 19], [12, 8], [20, 15], [6, 10], [6, 9], [3, 19], [7, 17], [6, 3],
#           [18, 18], [5, 15], [13, 15], [9, 1], [11, 3], [9, 17], [15, 10], [18, 11], [4, 14], [16, 4]], 108),
#     (10, [[4, 4], [10, 2], [5, 5], [5, 1], [1, 8], [9, 3], [9, 6], [8, 5], [1, 9], [4, 5]], 23),
#     (51, [[5, 32], [49, 28], [29, 35], [46, 27], [11, 15], [39, 7], [30, 8], [26, 27], [51, 50], [35, 27],
#           [15, 40], [40, 1], [47, 31], [22, 12], [41, 22], [4, 29], [51, 11], [40, 9], [22, 42], [9, 11],
#           [19, 33], [46, 29], [17, 40], [32, 20], [38, 26], [32, 51], [50, 40], [21, 15], [30, 23], [43, 9],
#           [2, 17], [31, 13], [13, 29], [27, 21], [23, 18], [48, 22], [6, 1], [43, 32], [51, 45], [27, 50],
#           [34, 28], [15, 32], [48, 27], [4, 19], [48, 3], [18, 6], [19, 43], [30, 15], [4, 21], [10, 10],
#           [13, 42]], 688),
#     (51, [[30, 37], [5, 34], [32, 14], [2, 33], [16, 9], [33, 19], [30, 8], [42, 37], [35, 40], [32, 24],
#           [51, 12], [8, 44], [23, 27], [5, 1], [33, 37], [48, 48], [36, 29], [35, 28], [30, 31], [49, 38],
#           [40, 16], [19, 9], [28, 33], [51, 34], [38, 26], [15, 24], [51, 39], [4, 30], [45, 31], [9, 37],
#           [8, 47], [42, 17], [22, 12], [34, 22], [19, 26], [35, 49], [16, 37], [51, 31], [9, 25], [21, 44],
#           [35, 38], [41, 5], [4, 44], [12, 4], [13, 41], [24, 39], [35, 15], [45, 45], [32, 20], [39, 2],
#           [14, 26]], 654),
# ]
#
# for coor_cnt, i_coors, ans in tests:
#     assert steps_count(coor_cnt, i_coors) == ans, f'Тест {coor_cnt, i_coors, ans}'
