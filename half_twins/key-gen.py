#!/usr/bin/python3
import random

numArray1 = []
numArray2 = []

while True:
    length = random.randint(7, 10)
    if (length%2) == 0:
        break

for i in range(int(length/2)):
    rand = random.randint(1,9)
    numArray1.append(rand)
    numArray2.append(rand)
for i in range (length-int(length/2)):
    while True:
        rand1 = random.randint(0,9)
        rand2 = random.randint(0,9)
        if rand1 != rand2:
            numArray1.append(rand1)
            numArray2.append(rand2)
            break
n1 = ''.join(str(n) for n in numArray1)
n2 = ''.join(str(n) for n in numArray2)
n1 = int(n1)
n2 = int(n2)
print("Key 1 - {}".format(n1))
print("Key 2 - {}".format(n2))
    
        
