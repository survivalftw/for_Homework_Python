import os
os.system('cls')

def rhytm(input_text):
    separated = input_text.lower().split()
    vowel_symbols = []
    for word in separated:
        same_vowels = len([i for i in word if i in 'аеёиоуыэюя'])
        vowel_symbols.append(same_vowels)
    if len(set(vowel_symbols)) == 1:
        return "Парам пам-пам"
    else:
        return "Пам парам"

input_text_to_test = str(input('Input a poem text: '))
print (rhytm(input_text_to_test))