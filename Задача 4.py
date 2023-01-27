# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

def zhuravliki_ratio(birds):
    Katya = birds / 2
    Petya = Katya / 2
    Serezha = Petya
    return Katya, Petya, Serezha


birds = 22
print('Katya: {}, Petya: {}, Serezha: {}'.format(*zhuravliki_ratio(birds)))
