# Задача 2: Найдите сумму цифр трехзначного числа.

def sum_of_digits(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    return round(sum, 2)


def input_number():
    return float(input('Введите число: '))


print('Сумма цифр числа:', sum_of_digits(input_number()))
