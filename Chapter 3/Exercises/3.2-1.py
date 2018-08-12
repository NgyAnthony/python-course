numbers = [3, 12, 34, 17, 21, -31, -12, -10]
def odd_number():
    for number in numbers:
        if number % 2 == 0:
            print(number, "is pair.")
        else:
            print(number,"is odd")

def sum_pos():
    sum_even = 0
    for number in numbers:
        if number % 2 == 0:
            sum_even += number
            print(number, "is pair.")
        else:
            print(number,"is odd")
    print(sum_even, "is the sum")

def sum_min():
    sum_minus = 0
    for number in numbers:
        if number > 0:
            continue
        else:
            sum_minus += number
    print(sum_minus, "is the sum.")

sum_min()