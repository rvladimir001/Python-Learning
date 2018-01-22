# -*- coding: utf- 8 -*-
"""ax^2+bx+c=0

a,b,c - коэффициенты
D - дискриминант.
D = b^2(в квадрате) - 4 × a × c

x1 = (-b + корень из D) / 2 × a
x2 = (-b - корень из D) / 2 × a
    Помним что, если

        D > 0 , 2 корня
        D = 0 , 1 корень (x = -b/(2 × a))
        D < 0 , нет корней
"""
import math
voln = "*"*50
print(voln)

a = int(input("[+] Введите a => "))
b = int(input("[+] Введите b => "))
c = int(input("[+] Введите c => "))
if a==0:
    print ("Не может быть нулем. Повторите ввод!")
    a = int(input("[+] Введите a => "))
else:
    print(voln)

D = b**2 - (4*a*c)

if D > 0:
    x1 = (-b + math.sqrt(D))/(2*a)
    x2 = (-b - math.sqrt(D))/(2*a)
    print("[!] Первый корень: ", x1)
    print("[!] Второй корень: ", x2)
elif D == 0:
        x = (-b)/(2*a)
        print("[!] Корень: ", x)
elif D < 0:
        print("[!] Корней нет!")
