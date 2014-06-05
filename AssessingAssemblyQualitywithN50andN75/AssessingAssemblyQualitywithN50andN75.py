dnastrings = []
with open('rosalind.txt') as f:
        for line in f:
            dnastrings.append(line.strip())

totallength = 0
for i in dnastrings:
    totallength += len(i)
print(totallength)

dnanumbers = [len(i) for i in dnastrings]
dnanumbers.sort()
print(dnanumbers)

for i in range(len(dnanumbers),0,-1):
    if sum(dnanumbers[i:]) > totallength/2:
        print(dnanumbers[i])
        break

for i in range(len(dnanumbers),0,-1):
    if sum(dnanumbers[i:]) > totallength*.75:
        print(dnanumbers[i])
        break
input()
