# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

def zhuravliki_ratio(number):
    Katya = number / 2
    Petya = Katya / 2
    Serezha = Petya
    return Katya, Petya, Serezha


def input_number():
    return int(input('Введите количество журавликов: '))


print('Катя: {}, Петя: {}, Сережа: {}'.format(*zhuravliki_ratio(input_number())))
