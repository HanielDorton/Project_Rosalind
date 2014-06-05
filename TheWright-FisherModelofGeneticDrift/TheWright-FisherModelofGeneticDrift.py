import math

population = 7
total = population*2
dominant = 8
percentage = (total-dominant)/total
gens = 5
atleastamountofrec = 7

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



results = []
for i in range(1,total+1):
    results.append([binomial(i,total,percentage), i])
print(results)

for i in range(gens-1):
    results =  generations(results)

answer = 0

for result in results:
    if result[1] > atleastamountofrec-1:
        answer += result[0]
print(answer)
