def sum_wonumb():
    numbers = [12, 17, 18, 29, 33, 22, 87]
    even_numbers = []
    odd_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers += [number]
        else:
            odd_numbers += [number]

    total = sum(even_numbers + odd_numbers) - even_numbers[0]
    print(even_numbers, "is even")
    print(odd_numbers, "is odd")
    print(total, 'is the sum without the first even number')





sum_wonumb()

#I don't get ex5 and I already accidentlaly did ex6.