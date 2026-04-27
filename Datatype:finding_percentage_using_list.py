x=int(input())
dict1={}
sums=0
for i in range(0,x):
    arry=[]
    list2=[]
    ins=input()
    arry=ins.split()
    n=arry[0]
    del arry[0]
    list2=[float(item) for item in arry]
    dict1[n]=list2
name=input()
for j in dict1[name]:
    sums+=j
ans=sums/3
print("{:.2f}".format(ans))
