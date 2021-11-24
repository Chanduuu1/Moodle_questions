l = []
l = input("").split()
k=0
while len(l) > 1:
    if l[k] != '+' and l[k] != '-' and l[k] != '*' and l[k] != '/':
        k = k+1

    elif l[k] == '+':
        a = float(l[k-2]) + float(l[k-1])
        l.pop(k)
        l.pop(k-1)
        l.pop(k-2)
        l.insert(k-2,a)
        k = 0

    elif l[k] == '-':
        a = float(l[k-2]) - float(l[k-1])
        l.pop(k)
        l.pop(k-1)
        l.pop(k-2)
        l.insert(k-2,a)
        k = 0 

    elif l[k] == '*':
        a = float(l[k-2]) * float(l[k-1])
        l.pop(k)
        l.pop(k-1)
        l.pop(k-2)
        l.insert(k-2,a) 
        k = 0

    elif l[k] == '/':
        a = float(l[k-2]) / float(l[k-1])
        l.pop(k)
        l.pop(k-1)
        l.pop(k-2)
        l.insert(k-2,a)
        k = 0

    if len(l) == 1:
        print(int(l))