n = int(input('Input list lenght: '))
Given_list = [int(input('Input list element: ')) for i in range (n)]
print (Given_list)
Track_number = int(input('Input a number to track in list: '))
print (f'Number {Track_number} occurs in list {Given_list.count(Track_number)} times')