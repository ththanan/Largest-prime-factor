round = 0
prime = []

for Number in range (1, int(600851475143 / 2)):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count += 1
            break
            round += 1

    if (count == 0 and Number != 1):
        prime.append(Number)
        if 600851475143 % Number == 0:
            print(Number)
    Number += 1