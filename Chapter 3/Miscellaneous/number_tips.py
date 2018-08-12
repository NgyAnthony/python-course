import random
joe = random.Random()

#Method 1
#numbers = []
#for _ in range (10000000):
#    num = joe.randrange(1000)
#    numbers.append(num)

#total = sum(numbers)
#print(total)

#Method 2
tot = 0
for _ in range(10000000):
    num = joe.randrange(1000)
    tot += num
print(tot)