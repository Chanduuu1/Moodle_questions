nStudents = int(input())
markList = []
orderingList = []
resultList = []
dummyList = []
markList2 = []

# This is for getting input from users!
for j in range(0,nStudents):
    nSubjects = int(input())
    for i in range(0,nSubjects):
        subjectName = input()
        subjectMarks = float(input())
        dummyList.append(subjectName)
        dummyList.append(subjectMarks)
    markList.append(dummyList)
    markList2 = markList
    dummyList = []


#This is for storing sunjects in which student fails and in the end i will count the number of repetation of that particular subject so as to get number of student failed in that subject!
for i in range(0,nStudents):
    for j in range(1,6,2):
        if markList[i][j] < 50:
            dummyList.append(markList[i][j-1])
        else:
            continue
            

# I just made this list in order to get all subjects in 1 single order as it was recieved in during input, then i will remove dupplicate element. why? u will know later
for i in range(0,nStudents):
    for j in range(0,6,2):
        orderingList.append(markList2[i][j])


# made unique subjects in ordeer of the input
dummyList2 = []
for i in orderingList:
    if i not in dummyList2:
        dummyList2.append(i)

# Counted number of failure in that particular subject and made detailed entry in a list
for i in dummyList2:
    f_In_1st = dummyList.count(i)
    resultList.append(i)
    resultList.append(f_In_1st)

#finally printing line by line
x = len(resultList)
for i in range(0,x):
    print(resultList[i])
    
    
    
# this is for counting number of student failed in atleast 1 subject!    
a=0    
for i in range(0,nStudents):

    for j in range(1,6,2):
        if markList[i][j] < 50:
            a = a + 1
            break               # agar ek bhi fail hua malum chala toh a  ko increment by 1 and go to next student outer for loop se transverse karenge aagle stud pe
        else:
            continue
print(a)
# issi ke sath prashna ka jaawab poorna