with open('input.txt', 'r') as f:
    m = f.readline()
    n = f.readline()
prenume=list(m.split(','))
varsta=list(n.split(','))
prenume[6]='Vio'
#Punctul a
print('         Punctul a           ')
a=''
for i in range(len(prenume)):
    print(str(prenume[i]), 'are varsta de', str(varsta[i]), 'de ani')
#Punctul b
print('         Punctul b           ')
prenume.extend(['Andreea', 'Ioan'])
varsta.extend([34, 23])
print(prenume, varsta, sep='\n')
#Punctul c
print('         Punctul c           ')
prenume.pop(2)
varsta.pop(2)
print(prenume, varsta, sep='\n')
#Punctul d
print('         Punctul d           ')
print('Primele trei elemente: ', prenume[:3])
#Punctul e
print('         Punctul e           ')
print('Lista inversata: ', prenume[::-1])
#Punctul f
print('         Punctul f           ')
print(prenume[2],' ', varsta[2], '\n', prenume[4],' ', varsta[4], '\n', prenume[:5], '\n', varsta[:5], sep='')