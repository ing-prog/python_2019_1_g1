# Определение(иициализация функции) - это скелет. Нельзя путать с вызовом функции
def my_function(n1, n2):  # def имя_функции(параметры, которые передаем в функцию):
    # Тело функции - код, который будет исполняться, при вызове функции
    sum1 = n1 + n2
    raz = n1 - n2
    umn = n1 * n2
    del1 = n2 / n1
    return [sum1, raz, umn, del1] # Результат, который мы хотим вернуть из функции. В данном случае это список

# Вызов функции
spisok = my_function(10, 100)


def factorial(n):
    rez = 1
    for i in range(1, n + 1):
        rez = rez * i
    return rez


a = factorial(5)
print(a)
