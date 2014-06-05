from ReverseSequence import reverse

currentdict=[]
with open('1rosalind.txt') as f:
        for line in f:
                currentdict.append(line.strip())
'''create setS containing all non duplicate items of the strings
and the reverse complements of the strings
'''
seconddict = []
for i in currentdict:
    seconddict.append(reverse(i))
setS = [i for i in currentdict]
for a in seconddict:
    setS.append(a)
setS = list(set(setS))
#print(setS)

'''
construct the graph
'''

for i in setS:
    print('(', end='')
    print(i[:-1], end='')
    print(',',i[1:], end ='')
    print(')')

