vowels = ['a', 'e', 'i', 'o', 'u']
word = 'Acido Desoxirribonucleico'

for letter in word.lower():
    if letter in vowels:
        print(letter)
