x = int(input('Input sum of two secret natural numbers: '))
y = int(input('Input multiplication of two secret natural numbers: '))
if x == 2 and y == 1:
    print("Secret numbers are", x, "and", y)
else:
    for i in range(x):
        for j in range(y):
            if x == i + j and y == i * j:
                print("Secret numbers are", i, "and", j)
