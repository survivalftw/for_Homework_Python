NumberA = int(input('Input number A: '))
NumberB = int(input('Input number B: '))
def sum_recursive(a, b):
    if a == 0 and b == 0:
        return a
    elif b > a:
        return sum_recursive(a, b-1) + 1
    elif a > b:
        return sum_recursive(a-1, b) + 1
    elif a == b:
        return sum_recursive(a-1, b-1) + 1 + 1
if NumberA < 0 or NumberB < 0:
    print('Error: input only positive numbers')
else:
    print(sum_recursive(NumberA, NumberB))