#Задача с презентации для цикла while
i = 0
while i < 5:
    a, b = input(), input()
    a = int(a)
    b = int(b)
    if (a == 0) and (b == 0):
        break  # досрочно завершаем цикл
    print(a * b)
    i += 1

"""Это еще один вид комментария. Все, что находтся внутри кавычек(три слева, три справа) как таких ", так и таких ' не обрабатывается python"""

'''
#Задача с презентации для цикла ащк
a, b = int(input()), int(input())
s = 0
step = 1
if a % 2 == 0:  # Выбираем шаг
    step = 2
for i in range(a, b + 1, step):
    s += i
print(s)
'''

"""
# Вывести треугольник из звезд
n = int(input())
c = 1
while c <= n:
    print('*' * c)
    c += 1
"""

'''
# Посчитать сумму чисел от a до b
a = int(input())
b = int(input())
s = 0
i = a
while i <= b:
    s += i
    i += 1
print(s)
'''

'''
# Выведите все нечётные числа от A до B включительно, в порядке убывания. В этой задаче можно обойтись без инструкции if
a, b = int(input()), int(input())
if a % 2 == 0:
    a=a-1
for i in range(a,b-1,-2):
    print(i)
'''

"""
# По данному натуральному n вычислите сумму 13+23+33+...+n3.
n = int(input())
s=0
for i in range(n+1):
    s+=i*i*i
print(s)
"""
