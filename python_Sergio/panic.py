phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
#My code here
#Esta es una manera de resolver el ejercicio que les mandé
#ok, gracias :v
undertaker = ['D', "'", ' ', 'p', 'i', 'c', '!']
for letter in undertaker:
    if letter in plist:
        plist.remove(letter)
        plist.pop()
plist.append('p')
plist.insert(2, ' ')
#End of my code
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)