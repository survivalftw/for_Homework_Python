
n = int(input('Input the number N: '))
i = 0
print("These numbers (2^n where n is natural number) are less than N:")
while 2 ** i <= n:
    print(2 ** i)
    i += 1