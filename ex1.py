a = "All "
b = "work "
c = "and "
d = "no "
e = "play "
f = "makes "
g = "Jack "
h = "a "
i = "dull "
j = "boy."
# Adds all variables
print(a + b + c + d + e + f + g + h + i + j)
print(6 * (1 - 2))

init_invest = input("Please enter your initial investment.")
r = input("Please enter your annual nominal interest rate.")
n = input("Please enter the number of times the interest is compounded per year")
t = input("Please enter the number of years.")
#init_invest = 500
#r = 0.01
#n = 1
#t = 10
print(int(init_invest) * (1+ float(r) / int(n)) ** (int(n) * int(t)))
