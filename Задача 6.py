# Задача 6: Вам требуется написать программу, которая проверяет счастливость билета.

def check_ticket(bool):
    return 'Это счастливый билет' if bool == True else 'Это обычный билет'


def comparison_of_halfs(number):
    return sum([int(x) for x in str(number)[:3]]) == sum([int(x) for x in str(number)[3:]])


def input_number():
    return int(input('Введите 6-значный номер билета: '))


print(check_ticket(comparison_of_halfs(input_number())))
