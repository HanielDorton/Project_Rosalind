import math

with open('rosalind.txt') as f:
    for line in f:
        line = line.strip()
        line = line.split()
for w in range(len(line)):
    line[w] = int(line[w])


population = 19
total = population*2
gens = 3


def binomial(number, total, percent):

    answer = (percent**number) * ((1-percent)**(total-number))
    secondanswer = answer*(math.factorial(total))/(math.factorial(number)*math.factorial(total-number))    
    return secondanswer


def generations(results):
    nextgeneration = []
    for result in results:
        newpercent = result[1]/total
        for x in range(1,total+1):
            nextgeneration.append([binomial(x,total,newpercent)*result[0], x])
    return nextgeneration            

answers=[]
for w in line:
    thisanswer=[]
    percentage = w/total
    results = []
    for i in range(1,total+1):
        results.append([binomial(i,total,percentage), i])

    answer = 0
    for result in results:
        answer+= result[0]
    thisanswer.append(math.log10(1-answer))

    for i in range(gens-1):
        results =  generations(results)
        answer = 0
        for result in results:
            answer += result[0]
        #print(answer)
        thisanswer.append(math.log10(1-answer))
    answers.append(thisanswer)

#print(answers)
for i in range(len(answers[0])):
    for x in range(len(answers)):
        print(answers[x][i], end= ' ')
    print()
