inputs = []
sums = []
i = 0
y = 0.0

inputN = int(input(print("How many inputs?")))

while i<inputN:
    inputs.append(int(input(print("Write an input: "))))
    i+=1

if i == inputN:
    i = 0

sumN = int(input(print("How many sums?")))
if sumN == 0:
    summed = sum(inputs)
else:
    while i<sumN:
        sums.append(int(input(print("Write a sum value: "))))
        i+=1

if i == sumN:
    i = 0
    

if sumN == 0:
    print(summed)
else:
    summed = sum(x * y for x, y in zip(inputs, sums))



if summed <= 0:
    y = -1
    print(f"Result of method 1: {y}")
elif summed > 0:
    y = 1
    print(f"Result of method 1: {y}")

if summed < 0:
    y = 0
    print(f"Result of method 2: {y}")
elif summed >=0 and summed <=1:
    y = summed
    print(f"Result of method 2: {y}")
elif summed > 1:
    y = 1
    print(f"Result of method 3: {y}")

if summed >= 0:
    y = 1 - (1/(1+summed))
    print(f"Result of method 3: {y}")
elif summed < 0:
    y = -1 + (1/(1-summed))
    print(f"Result of method 3: {y}")