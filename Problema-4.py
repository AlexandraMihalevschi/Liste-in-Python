n = int(input('Dati numar: '))
a=[]
for i in range(2,n+1):
    c=0
    for j in range(2,i):
        if i%j!=0:
            c+=1
    if c==i-2:
        a.append(i)
print(f'Numere prime. in total sunt: {c} de cifre')
print('Numerele prime sunt', str(a))