"""
Задача 4
Написать функцию, принимающую длину стороны квадрата и рассчитывающую периметр
квадрата, его площадь и диагональ. Сделать два и более варианта функции, которые
должна отличаться количеством возвращаемых переменных. Не забыть про проверки
входных данных в самой функции.

"""
num1 = float(input("Введите длину стороны квадрата: \n"))

print("Периметр равен {}".format(num1 * 4))
print("Площадь равна {}".format(num1 ** 2))
print("Диагональ равна {}".format(((num1**2)+(num1**2))**0.5))

print("2" * 50)
#а теперь извращаемся с функциями
def quad():
    print("Периметр равен {}".format(num1 * 4))
    print("Площадь равна {}".format(num1 ** 2))
    print("Диагональ равна {}".format(((num1**2)+(num1**2))**0.5))
quad()

print("3" * 50)

def line():
    try:
        x = float(input("Введите длину: \n"))
        perimeter = x * 4
        ploshad = x ** 2
        diagonal = ((2 * x**2) ** 0.5) # смысла подключать math не вижу
        print("Периметр равен {}, площать равна {}, диагональ равна {}".format(
        perimeter, ploshad, diagonal))
    except ValueError:
        print("Вы ввели неверные данные, повторите.")
        line()
print("Ну что посчитаем? Y/Да  N/Нет")
inp = input()
if inp == "Y" or inp == "Д" or inp == "y" or inp == "д":
    line()
elif inp == "N" or inp == "Н" or inp == "н" or inp == "n":
    print("Ну нет так нет.")
    exit
else:
    exit
#print(perimeter, ploshad, diagonal)
#print(line())
