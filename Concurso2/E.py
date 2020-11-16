import random
r = ['R','A']
v = ['V','R']
a = ['A','V']
color=input('')
color=color[0]
color=color.upper()
state = int(input(''))
res=''
if state >= 1 and state <= 1000:
    for i in range(state):
        if color=='R':
            res=(r[1])#A
            color=res
        elif color=='V':
            res=(v[1])
            color=res
        elif color=='A':
            res=(a[1])
            color=res
    print(res)
