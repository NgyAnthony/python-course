n = 25
threshold = 0.1
approximation = n/2 # Start with some or other guess at the answer
while True:
    better = (approximation + n/approximation)/2
    print(approximation)
    if abs(approximation - better) < threshold:
        print(better)
        break
    approximation = better

#I don't get how TF this algorithm works.
#Seriously, how do you even find this ?