from random import randint
n = int(input('Input list 1 lenght: '))
m = int(input('Input list 2 lenght: '))
Given_list_1 = [randint (0, 99) for _ in range (n)]
Given_list_2 = [randint (0, 99) for _ in range (m)]
Merged_list = Given_list_1 + Given_list_2
print ('List 1 is', Given_list_1)
print ('List 2 is', Given_list_2)
Number_Memory_Cell = min(Merged_list)
Result_list = [Number_Memory_Cell]
while Number_Memory_Cell != max(Merged_list):
    Number_Converter = max(Merged_list)
    for i in range(len(Merged_list)):
        if Merged_list[i] > Number_Memory_Cell:
            Number_counter = Merged_list[i]
            if Number_Converter >= Number_counter:
                Number_Converter = Number_counter
    Number_Memory_Cell = Number_Converter
    Result_list.append (Number_Memory_Cell)
print ('The result ascending list with no repeats is', Result_list)