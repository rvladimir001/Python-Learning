"""
Напишите программу, которая получает на вход три целых числа, по одному числу в
строке, и выводит на консоль в три строки сначала максимальное, потом минимальное,
после чего оставшееся число.

На ввод могут подаваться и повторяющиеся числа.
"""

a,b,c=int(input()),int(input()),int(input())
spisok=[a,b,c]
spisok.sort()
print (spisok[2],spisok[0],spisok[1], sep="\n")
