"""
Задача 3
Использовать функции из задач 1, 2 для решения задания 2 из урока 2: Программа,
которая считывает два числа и выводит их сумму
"""
print("Введите числа которые нужно сложить:")
def sumNum():
    try:
        #объявим значения глобальными, чтобы можно было использовать за пределами функции
        global num1, num2
        num1 = int(input("Введите число А\n"))
        num2 = int(input("Введите число В\n"))
        #Выведем сложение в теле функции
        print("Сумма в теле функции {} + {} = {}".format(num1, num2, (num1+num2)))
    except ValueError:
        print("Вы ввели не число, попробуйте еще раз.")
        sumNum()
sumNum()
print("Сумма за пределами функции {} + {} = {}".format(num1, num2, (num1+num2)))
