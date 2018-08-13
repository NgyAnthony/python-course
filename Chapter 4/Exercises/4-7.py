import math


def sum_to(n):
    total = 0
    for _ in range(n):
        total += _
        print(total+n)
    return total


sum_to(10)

def area_of_circle(r):
    area = math.pi * (r ** 2)
    print(area)

area_of_circle(5)