from random import randint
n = int(input('Input list lenght: '))
list_random = [randint (0, 99) for _ in range (n)]
print (list_random)
min_number_compare = int(input('Input min number for cut off: '))
max_number_compare = int(input('Input max number for cut off: '))
for i in range(len(list_random)):
    if min_number_compare <= list_random[i] <= max_number_compare:
        print(i)