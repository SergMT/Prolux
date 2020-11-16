numP = int(input(''))
pelotas = input('').split()
prom=0
sum=0
for index in range(len(pelotas)):
    sum+=int(pelotas[index])
    # if int(pelotas[index])==1:
    #     res=1
    # else:
prom = int(sum/numP)

if prom==int(pelotas[0]):
  print (int(prom))
else:
  print (int(sum))

# 3r 2a 1v = 3/6 