#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Задание №3
# Одноклеточная амеба каждые три часа делится на 2 клетки.
# Определить, сколько будет клеток через 6 часов.


if __name__ == '__main__':
    n = int(input("Enter the number of amebas... "))
    hours = int(input("Enter the hours... "))
    result = n
    time = hours
    while time >= 3:
        result += n
        time -= 3

    print(f"The number of {n} amoebas after {hours} hours is {result}")
