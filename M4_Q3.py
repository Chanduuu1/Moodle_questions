numOfList = int(input())
lenOfList = int(input())
L = []
for i in range(0,numOfList):
    l = list(input().split())
    L.append(l)
    l = []

valueOfIndex = int(input())
valueOfString = input()

for i in L:
    if i[valueOfIndex] == valueOfString:
        print(type('[%s]'%(','.join(i))))   # its not a list par se- we printed a string!because list was giving some type of error anyway you learnt %s function!
    else:                                   # join() join karta hai itmes of a list tuple dict set etc kisi bhi argument se jo hum usse pass kare .join() leekhne se pehle!
        continue;