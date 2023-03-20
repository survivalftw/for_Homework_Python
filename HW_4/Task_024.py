n = int(input('Input bush count: '))
arr = list()
for i in range(n):
    x = int(input('Input berry count for each bush: '))
    arr.append(x)
arr_count = list()
for i in range(len(arr) - 1):
    arr_count.append(arr[i - 1] + arr[i] + arr[i + 1])
arr_count.append(arr[-2] + arr[-1] + arr[0])
print('The maximum berry count collectable from 3 adjacent bushes is', max(arr_count))