# -*- coding: utf- 8 -*-
chislo=834.23
#нужно вывести сотни, десятки и еденицы

sotni=float(chislo//100)
desyatki=float((chislo%100)//10)
edenicy=float(((chislo%100)%10)//1)
ostatok=float(((chislo%100)%10)%1)
print("sotni=", sotni)
print("desyatki=", desyatki)
print ("edenicy=", edenicy)
print("ostatok=", ostatok)
summ=float(desyatki+sotni+edenicy)
print("summa chisel=", summ)
