# If you dont know ow man lists you may be needing then for that create a main list and in it add 3 emoty lists and in it add values and in end only take
# sub lists! follow!?

sum=0
numOfTuples = int(input("Number of lists you want: "))
mainList = []
for i in range(0,numOfTuples):
    subList = []
    mainList.append(subList)


for j in range(0,numOfTuples):
    numOfItesm = int(input("Enter the number of elements you want to enter in this list: "))    
    for k in range(0,numOfItesm):
        ele = input()
        mainList[j].append(ele)


mainList2 = []
for i in range(0,numOfTuples):
    subList2 = []
    mainList2.append(subList2)


for i in range(0,numOfTuples):
    mainList2[i].append(mainList[i][0])


for j in range (0,numOfTuples):
    temp = len(mainList[j])
    for k in range(2,temp,2):
        n = int(mainList[j][k])
        sum += n
    
    mainList2[j].append(sum)
    sum=0

for i in range(0,numOfTuples):
    mainList2.append(tuple(mainList2[i]))

del mainList2[0:numOfTuples]

print(tuple(mainList2)) 