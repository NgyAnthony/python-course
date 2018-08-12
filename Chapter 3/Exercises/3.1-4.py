numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

def new_line():
    for number in numbers:
        print(number)

def square():
    for number in numbers:
        print(number, number ** 2)

def total_add():
    total = 0
    for number in numbers:
        total += number
    print(total)

def multiplied_total():
    total_multi = 1
    count = 0
    for number in numbers:
        count += 1
        total_multi *= number
    print(total_multi)