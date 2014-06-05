'''Open the file and inport the data as three strings in a list'''
question = ['','','']
count = 0
with open('1rosalind.txt') as f:
        for line in f:
            if '{' in line:
                count+=1
                question[count] += line.strip().replace('{', '').replace('}', '')
            else:
                question[count] += line.strip().replace('{', '').replace('}', '')
'''make master list of all the numbers in the total range'''
masterset = [i for i in range(1,int(question[0])+1)]


def makelists(set):
    '''for each string returns a list'''
    returnset = set.split(',')
    for i in range(len(returnset)):
        returnset[i] = int(returnset[i])
    return returnset

def pp(inset):
    '''prints the list so they look like sets'''
    return(str(inset).replace('[', '{').replace(']', '}'))
    
def union(seta, setb):
    answer = seta[::]
    for i in setb:
        answer.append(i)
    return list(set(answer))

def intersection(seta, setb):
    answer = []
    for a in seta:
        for b in setb:
            if a == b:
                answer.append(a)
    return answer

def setdifference(seta, setb):
    answer = []
    for a in seta:
        if a  not in setb:
            answer.append(a)
    return answer
    
seta = makelists(question[1])
setb = makelists(question[2])

print(pp(union(seta, setb)))
print(pp(intersection(seta, setb)))
print(pp(setdifference(seta, setb)))
print(pp(setdifference(setb, seta)))
print(pp(setdifference(masterset, seta)))
print(pp(setdifference(masterset, setb)))

