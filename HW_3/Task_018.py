from random import randint
n = int(input('Input list lenght: '))
Given_list = [randint (-1000, 1000) for _ in range (n)]
print (Given_list)
x = int(input('Input a number to track closest ones to in list: '))
Target_number = 0
Difference = abs(Given_list[0] - x)
for i in range(len(Given_list)):
    if Difference > abs(Given_list[i] - x):
        Difference = abs(Given_list[i] - x)
        Target_number = Given_list[i]
print ('The closest number to be tracked is', Target_number)