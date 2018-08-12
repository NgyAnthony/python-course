threshold = 1e-7
a = int(input("First value"))
b = int(input("Second value"))
c = int(input("Third value"))

a = a ** 2
b = b ** 2
c = c ** 2

x = a + b
y = b + c
z = c + a

if abs(x-c) < threshold or abs(y-a) < threshold or abs(z-b) < threshold:
    print(True)
else:
    print(False)
