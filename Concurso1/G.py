a = input('').split()
t=[]
res = 0
for i in range(len(a)):
  temp = input('')
  t.append(temp)

for i in range(len(t)):
  if t[i]=="hole in one":
    res += pow(int(a[i]), 0)
  if t[i]=="condor":
    res += int(a[i])-4
  if t[i]=="albatross":
    res += int(a[i])-3
  if t[i]=="eagle":
    res += int(a[i])-2
  if t[i]=="birdie":
    res += int(a[i])-1
  if t[i]=="par":
    res += int(a[i])#queda igual
  if t[i]=="bogey":
    res += int(a[i])+1
  if t[i]=="double bogey":
    res += int(a[i])+2
  if t[i]=="triple bogey":
    res += int(a[i])+3
print(res)