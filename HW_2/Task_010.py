n = int(input('Input number of coins: '))
count_eagle = 0
count_tail = 0
for i in range(n):
    x = int(input('Input 0 for eagle coin and 1 for tail coin: '))
    if x == 0:
        count_eagle += 1
    else:
        count_tail += 1
if count_tail > count_eagle:
    print("It is needed to flip at least", count_eagle, "eagle coins to turn every coin to tail position")
else:
    print("It is needed to flip at least", count_tail, "tail coins to turn every coin to eagle position")