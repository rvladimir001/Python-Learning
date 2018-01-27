"""
Задача 2

Сделать задачу 5 из урока 4 с циклом for и обращением к строке
"""


num = input("Введите число =>")
fignya = 0
for i in num:
    if int(num) % 2 == 0:
        fignya +=1
    num = int(num) //10
print("Тутачки {} четных цифр".format(fignya))
