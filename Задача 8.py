# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек
# отломить k долек, если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).

def check_rectangle(values):
    return values[2] < values[1] * values[0] and (values[2] % values[0] == 0 or values[2] % values[1] == 0)


def return_answer(bool):
    return 'Такое количество k долек можно отломить' if bool else 'Такое количество k долек отломить не получится'


def input_values():
    n, m, k = int(input('Введите n: ')), int(input('Введите m: ')), int(input('Введите k: '))
    return n, m, k


print(return_answer(check_rectangle(input_values())))
