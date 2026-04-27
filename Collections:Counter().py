from collections import Counter
x=int(input())
col=input()
list1=[int(j) for j in col.split()]
y=int(input())
sums=0
for i in range(0,y):
    l=[]
    pur=input()
    l=[int(z) for z in pur.split()]
    quan=Counter(list1)
    if(quan[l[0]]!=0):
        sums+=l[1]
        list1.remove(l[0])
print(sums)
