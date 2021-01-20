a = [int(x) for x in input("Dati sirul: ").split()]
print("Sirul:" ,a)
b = sorted(a)
print("Sirul in ordine crescatoare:", b)
c=a
c.sort(reverse=True)
print("Sirul in ordine descrescatoare:",c)
print("Sirul are lungimea de", len(a))
print("Valoarea maxima: ", max(a))
print("Valoarea minima: ", min(a))
d=a
d.extend([111])
print("Noul sir: ", d)
a.remove(111)
a.insert(1, 222)
print("Noul sir:", a)