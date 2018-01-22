# -*- coding: utf- 8 -*-
"""
Напишите код который будет спрашивать 3 возраста и определять самый большой,
маленький и средний.

"""
a = int(input("Введите первый возраст --> "))
b = int(input("Введите второй возраст --> "))
c = int(input("Введите третий возраст --> "))
line = "~"*20
print("Прекрасно! Теперь отсортируем их по убыванию.")
print(line)
if a==b==c:
    print("Они одинаковые")
elif a>b>c:
    print(a, b, c)
elif a<b<c:
    print(c, b, a)
elif b>c>a:
    print(b, c, a)
elif a>c>b:
    print(a, c, b)
elif c>a>b:
    print(c, a, b)
elif a==b>c:
    print(a, b, c)
elif a==b<c:
    print(c, a, b)
elif a>b==c:
    print(a, b, c)
elif a<b==c:
    print(b, c, a)
elif a==c>b:
    print(c, a, b)
elif a==c<b:
    print(b, a, c)

input("Для закрытия программы нажми Enter")
