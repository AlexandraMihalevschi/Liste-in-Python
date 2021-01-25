with open('input.txt', 'r') as f:
    a = f.readline()
b = a.split(',')
b = list(b)
b.sort()
i=0
x=''
with open('output.txt', 'w') as f:
    for i in b:
        x+=i+"\n"
        f.write(str(x))
        x=''