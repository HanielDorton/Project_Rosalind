months = 94
lifespan = 20

population = [[1,0]]
for i in range(lifespan-1):
    population.append([0,1])
#print(population)
for i in range((lifespan*months)+lifespan):
    population.append([0,0])
#print(population)

for month in range(months):
    for life in range(1, lifespan+1):
        currentpop = population[month][1]
        if life == 1:
            population[month + life][0] += currentpop
        else:
            population[month + life][1] += currentpop
            

#print(population)
answer = population[months-1]
print(answer)
print(answer[0]+answer[1])
