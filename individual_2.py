#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Задание №2
# Определить принадлежит ли точка кольцу определяемому окружностями
# x^2 + y^2 = 1 и x^2 + y^2 = 0.25

if __name__ == '__main__':
    x = float(input("Enter x... "))
    y = float(input("Enter y... "))
    if ((x ** 2 + y ** 2) <= 1) and ((x ** 2 + y ** 2) >= 0.25):
        print(f"The point ({x}, {y}) belongs to the ring!")
    else:
        print(f"The point ({x}, {y}) does not belongs to the ring!")
