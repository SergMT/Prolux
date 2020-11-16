phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
#start
new_phrase = []
new_phrase.append(''.join(plist[1:3]))
new_phrase.append(' ')
new_phrase.append(''.join(plist[-5:-7:-1]))
new_phrase.insert(2, 't')
new_phrase = ''.join(new_phrase)
#end
print(plist)
print(new_phrase)
