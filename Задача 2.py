# Задача 2: Найдите сумму цифр трехзначного числа.

def sum_of_digits(number):
    sum = 0
    for x in range(number):
        sum += number % 10
        number //= 10
    return sum


a = 528
print(sum_of_digits(a))