"""
Задача 4

Найдите произведение цифр трехзначного числа, введёного с клавиатуре.
"""
#первый вариант
num = input("Введите число ->")
count =1
if int(num) < 1000 or int(num) >= 100:
    for i in num:   #идем по каждому символу в переменной
        count *= int(i)
    print("Произведение чисел числа {} равно {}".format(num, count))
else:
    print("Не верные данные.")

print("~" * 70)

#второй вариант
"""
n = int(input("Введите трехзначное число: "))

if int(n) < 1000:
    if int(n) >= 100:
        d1 = n % 10
        d2 = n % 100 // 10
        d3 = n // 100
        d = d1 * d2 * d3
        print("Произведение чисел числа {} равно {}".format(n, d))
    else:
        print("Не верные данные.")
else:
    print("Не верные данные.")
"""
