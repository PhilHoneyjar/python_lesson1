# Задача 6: Вам требуется написать программу, которая проверяет счастливость билета.

def comparison_of_halfs(number):
    return sum([int(x) for x in str(number)[:3]]) == sum([int(x) for x in str(number)[3:]])


ticket_number = 584945
print(comparison_of_halfs(ticket_number))