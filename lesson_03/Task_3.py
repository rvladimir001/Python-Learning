"""
Проверить, что хотя бы одно из чисел a или b оканчивается на 0.
"""
a = int(input("Введите первое число ->"))
b = int(input("Введите второе число ->"))
if a % 10 == 0 and b % 10 == 0:
    print("Числa {} и {} оканчиваются на ноль".format(a,b))
elif a % 10 == 0:
    print("Число {} оканчивается на ноль".format(a))
elif b % 10 == 0:
    print("Число {} оканчивается на ноль".format(b))
elif a % 10 !=0 and b % 10 !=0:
    print("Числа {} и {} не оканчиваются на ноль".format(a,b))