vowels = ['a', 'e', 'i', 'o', 'u']
word = 'Acido Desoxirribonucleico'
found = []

for letter in word.lower():
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)
