Number = int(input('Input a number: '))
PowerDegree = int(input('Input a power degree: '))
def power_degree_recursive(m, n):
    if m == 1:
        return m
    else:
        return n * power_degree_recursive(m-1, n)
print(power_degree_recursive(PowerDegree + 1, Number))