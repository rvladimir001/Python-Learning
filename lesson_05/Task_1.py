"""
Задача 1

Сделать задачу 4 из урока 4 с циклом for и обращением к строке
"""
num = input("Введите число ->")
count =1
if int(num) < 1000 or int(num) >= 100:
    for i in num:   #идем по каждому символу в переменной
        count *= int(i) #умножаем каждый численный символ в строке
    print("Произведение чисел числа {} равно {}".format(num, count))
else:
    print("Не верные данные.")

print("~" * 70)