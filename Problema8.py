n = str(input('Dati un numar: '))
a=[]
c=''
a.extend(n)
for i in range(len(a)):
    a[i]=int(a[i])
a=sorted(a)
for i in range(len(a)):
    if a[0]==0:
        a.pop(0)
        a.insert(1, 0)
    c=c+str(a[i])
print(c)