x=int(input())
l=[]
for i in range(0,x):
    l1=[]
    name=input()
    score=float(input())
    l1.append(name)
    l1.append(score)
    l.append(l1)
sortl=sorted(l, key=lambda x: (x[1],x[0]))
num=sortl[0][1]
for i in range(0,x):
    if(num!=sortl[i][1]):
        num=sortl[i][1]
        break
for i in range(0,x):
    if(num==sortl[i][1]):
        print(sortl[i][0])

