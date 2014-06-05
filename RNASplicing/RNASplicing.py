from Codon_Table import codon_table
import re
count = -1
currentdict=[]
with open('rosalind.txt') as f:
        for line in f:
                if '>' in line:
                    currentdict.append('')
                    count+=1
                else:
                    currentdict[count] += line.strip()

mainrna = currentdict[0]
del(currentdict[0])
#print('mainrna: ', mainrna)
for i in currentdict:
    mainrna = mainrna.replace(i, '')
#print('mainrna after removing splices:', mainrna)
mainrna = mainrna.lower()
mainrna2 =''
for i in mainrna:
    if i == 't':
        mainrna2 += 'u'
    else:
        mainrna2 += i

print('Lowercase and switch ts to us: ', mainrna2)

answer = ''
for i in range(0, len(mainrna2), 3):
    answer += codon_table[mainrna2[i:i+3]]
print(answer)
    
