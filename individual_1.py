#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Задание №1
# С клавиатуры вводится цифра (от 1 до 4). Вывести на экран
# названия месяцев, соответствующих времени года с номером
# (считать зиму временем года No 1).

import sys

if __name__ == '__main__':
    m = int(input("Enter the season number... "))
    if (m < 1) or (m > 4):
        print("Illegal value of m", file=sys.stderr)
        exit(1)
    if m == 1:
        print("Зима: \nдекабрь, январь, февраль.")
    elif m == 2:
        print("Весна: \nмарт, апрель, май.")
    elif m == 3:
        print("Лето: \nиюнь, июль, август.")
    elif m == 4:
        print("Осень: \nсентябрь, октябрь, ноябрь.")
