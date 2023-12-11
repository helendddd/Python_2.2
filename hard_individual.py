#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Задание повышенной сложности
# Вычисление значения специальной функции по ее разложению в ряд
# Первый интеграл Френеля

import math
import sys

if __name__ == '__main__':
    EPS = 1e-10
    x = float(input("Enter x... "))

    if x == 0:
        print("Illegal value of n", file=sys.stderr)
        exit(1)

    result = x
    sum = x
    n = 1

    while math.fabs(result) > EPS:
        result *= (-(x**4)*(math.pi/2)**2 * (4))/((4*n**2 + 6*n + 2)*(4*n + 5))
        sum += result
        n += 1
    print(sum)
