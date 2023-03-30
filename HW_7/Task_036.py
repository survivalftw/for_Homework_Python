import sys, os
os.system('cls')

def print_operation_table(operation, num_rows=6, num_columns=6):
    for row in range(1, num_rows + 1):
        print(*map(operation, [row] * num_columns, range(1, num_columns + 1)), sep='\t')

print(print_operation_table(lambda x, y: x * y))