# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

print("Введите число")
num = int(input())

def daysoftheWeek(num):
    if 6 <= num <= 7:
        print("Да")
    elif 0 < num < 6:
        print("Нет")
    else:
        print("такого дня недели нет")

daysoftheWeek(num)