with open('input.txt', 'r') as a:
    lista = a.readline()
a=lista
with open('output.txt', 'w') as a:
    a.write('Sirul- ')
    a.write(str(a))
b=list(lista)
b.sort()
with open('output.txt', 'w') as a:
    a.write('Sirul in ordine crescatoare- ')
    a.write(str(b))
c=list(lista)
c.sort(reverse=True)
with open('output.txt', 'w') as a:
    a.write('Sirul in ordine descrescatoare:')
    a.write(str(c))
i = len(list(lista))
with open('output.txt', 'w') as a:
    a.write('Lungimea sirului- ')
    a.write(str(i))
n = max(list(lista))
m = min(list(lista))
with open('output.txt', 'w') as a:
    a.write('Minimul- ')
    a.write(str(m))
    a.write('Maximul- ')
    a.write(str(n))
d=list(lista)
d.extend([111])
with open('output.txt', 'w') as a:
    a.write('Noul sir- ')
    a.write(str(d))
d.remove(111)
d.insert(1, 222)
with open('output.txt', 'w') as a:
    a.write('Noul sir- ')
    a.write(str(d))