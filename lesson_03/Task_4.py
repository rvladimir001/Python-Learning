"""
Дана следующая функция y = f(x):

  y = x + 1.5, при x > 10;
  y = 0, при x = 10;
  y = -x, при x < 10.
  Написать программу, определяющую значение y по введеному значению x.
"""
x = float(input("Введите Х ->"))
if x > 10:
    y = x + 1.5
    print("y=f(x) >>> y={}".format(y))
elif x == 10 or x == 0:
    y = 0
    print("y=f(x) >>> y={}".format(y))
elif x < 10:
    y = -x
    print("y=f(x) >>> y={}".format(y))
