# Расписание
#
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
#
# Как же Илье надоело учиться! Сначала школа, потом университет... Вот, наконец, наступил тот долгожданный день,
# когда Илье утром не надо ехать на учебу. Но, к несчастью для Ильи, оказалось, что после окончания университета
# начинается самое трудное — надо устраиваться на работу.
#
# Во всемирно известной фирме «Goondex», в которую устроился Илья, принято очень много работать, в частности, для
# сотрудников установлена шестидневная рабочая неделя. Но, в качестве бонуса, «Goondex» каждый год предлагает своим
# сотрудникам выбрать любой день недели в качестве выходного. В свою очередь, оставшиеся шесть дней недели будут
# рабочими.
#
# Илья сообразил, что с учётом государственных праздников (которые всегда являются выходными) с помощью правильного
# выбора выходного дня недели можно варьировать количество рабочих дней в году. Теперь он хочет знать, какой день
# недели ему следует выбрать в качестве выходного, чтобы отдыхать как можно больше дней в году, или, наоборот,
# демонстрировать чудеса трудолюбия, работая по максимуму.
#
# Формат ввода
# В первой строке входных данных находится одно целое число N (0 ≤ N ≤ 366) — количество государственных праздников.
# Во второй строке содержится одно целое число year (1800 ≤ year ≤ 2100) — год, в который необходимо помочь Илье.
# В каждой из последующих N строк расположено по паре чисел day month (day — целое число, month — слово, между day и
# month ровно один пробел), обозначающих, что день day месяца month является государственным праздником.
# В последней строке расположено слово  — день недели первого января в год year.
# Гарантируется, что все даты указаны корректно (в том числе указанный день недели первого января действительно является
# днём недели первого января соответствующего года year) и все дни государственных праздников различны.
#
# Формат вывода
# Выведите через пробел два дня недели — лучший и худший варианты дней недели для выходного (то есть дни недели, для
# которых достигается соответственно максимальное и минимальное количество выходных дней в году). Если возможных
# вариантов ответа несколько, выведите любой из них.
#
# Пример 1
# Ввод
# 2
# 2015
# 1 January
# 8 January
# Thursday
#
# Вывод
# Monday Thursday
#
# Пример 2
# Ввод
# 3
# 2013
# 1 January
# 8 January
# 15 January
# Tuesday
#
# Вывод
# Monday Tuesday
#
# Пример 3
# Ввод
# 3
# 2013
# 6 February
# 13 February
# 20 February
# Tuesday
#
# Вывод
# Tuesday Wednesday
#
# Примечания
# Рассмотрим подробно третий пример.
# 2013 год начинается и заканчивается во вторник (Tuesday), при этом на вторник приходится 53 дня года, а на все
# остальные дни недели –— по 52 дня. Все три государственных праздника выпадают на среду (Wednesday). Если Илья выберет
# в качестве выходного дня вторник, то в году у него будет 53 + 3 = 56 выходных дней (53 вторника и 3 государственных
# праздника). Если Илья выберет в качестве выходного дня среду, то у него будет только 52 выходных дня. Если же Илья
# выберет в качестве выходного дня любой другой день недели, то у него будет 52 + 3 = 55 выходных дней.
#
# Таким образом, лучший вариант для выходного дня — вторник, худший — среда, и единственным правильным ответом в данном
# примере является Tuesday Wednesday.
#
# В феврале 29 дней только в високосные года. Год является високосным, если он кратен 400, либо кратен 4 и не
# кратен 100.
# Например, 1996 и 2000 являются високосными, а 1999 и 1900 — нет.

import datetime

MONTHS = {
    'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,
    'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12
}

DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


weekday_cnt = [52 for _ in range(7)]

with open('input.txt', 'r', encoding='utf-8') as file:
    days_off = int(file.readline())
    cur_year = int(file.readline())
    for _ in range(days_off):
        i_num, month_name = file.readline().split()
        i_day = datetime.datetime(cur_year, MONTHS[month_name.lower()], int(i_num)).weekday()
        weekday_cnt[i_day] -= 1

    i_beginning_year = DAYS.index(file.readline().rstrip().lower())
    if is_leap_year(cur_year):
        if i_beginning_year == 6:
            weekday_cnt[0] += 1
        else:
            weekday_cnt[i_beginning_year + 1] += 1
    else:
        weekday_cnt[i_beginning_year] += 1

    best_case = weekday_cnt.index(max(weekday_cnt))
    worst_case = weekday_cnt.index(min(weekday_cnt))
    if best_case == worst_case:
        print(DAYS[0].capitalize(), DAYS[1].capitalize())
    else:
        print(DAYS[best_case].capitalize(), DAYS[worst_case].capitalize())
