Number = int(input('Input a number: '))
PowerDegree = int(input('Input a power degree: '))
def power_degree_recursive(m, n):
    if m == 0:
        return m + 1
    return n * power_degree_recursive(m-1, n)
print(power_degree_recursive(PowerDegree, Number))