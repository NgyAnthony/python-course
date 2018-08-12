n = -1340
r = n
count = 0


def even_numbers():
    """Identify even number"""
    char_digit = str(r)
    num_digit = char_digit[count]
    int_digit = int(num_digit)
    if int_digit % 2 != 0 or int_digit == 0:
        print(int_digit, "is not even.")
    elif int_digit % 2 == 0:
        print(int_digit, "is even.")


if n > 0:
    while n != 0:
        count += 1
        n = n // 10
        even_numbers()
    print("There is", count, "digits.")

elif n < 0 and n != -1:
    while n != -1:
        count += 1
        n = n // 10
        even_numbers()
    print("There is", count, "digits.")

else:
    count += 1
    print("There is", count, "digits.")
