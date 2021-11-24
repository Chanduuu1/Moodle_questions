l=[]
dupp=[]
n=int(input())
l=input("").split()
for i in range(0,n):
    ele=int(l[i])
    dupp.append(ele)

for i in range(1,n):
    leftList=dupp[0:i]
    rigtList=dupp[i+1:n]
    sL=sum(leftList)
    sR=sum(rigtList)
    if sL==sR:
        print(i)
        break
    elif i==n-1 and sL!=sR:
        print("0")
    else:
        continue;  