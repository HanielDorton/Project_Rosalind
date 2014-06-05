ls = []
linecount=-1
with open('rosalind_cons.txt') as f:
        for line in f:
            
                if '>' in line:
                        ls.append('')
                        linecount += 1
                else:
                        ls[linecount] += (line.strip())
A=[]
C=[]
G=[]
T=[]

for i in range(len(ls[1])):
    A.append(0)
    C.append(0)
    G.append(0)
    T.append(0)

for dnastring in ls:
    for i in range(len(dnastring)):
        if dnastring[i] == 'A':
            A[i] += 1
        elif dnastring[i] == 'C':
            C[i] += 1
        elif dnastring[i] == 'G':
            G[i] += 1
        elif dnastring[i] == 'T':
            T[i] += 1

solution=[]

for i in range(len(A)):
    solution.append('A')
    if C[i] > A[i]:
        solution[i] = 'C'
    if (G[i] > C[i]) and (G[i] > A[i]):
        solution[i] = 'G'
    if (T[i] > G[i]) and (T[i] > A[i]) and (T[i] > C[i]):
        solution[i] = 'T'

A = repr(A).replace(",", " ")
C = repr(C).replace(",", " ")
G = repr(G).replace(",", " ")
T = repr(T).replace(",", " ")

print(''.join(solution))
print('A: ', ''.join(str(A)))
print('C: ', ''.join(str(C)))
print('G: ', ''.join(str(G)))
print('T: ', ''.join(str(T)))
            
        
