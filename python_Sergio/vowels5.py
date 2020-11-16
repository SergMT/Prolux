vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Introduce una palabra para buscar sus vocales: ')
found = {}

for letter in word.lower():
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1
for k, v in sorted(found.items()):
    print(k,'was found', v, 'time(s)')
