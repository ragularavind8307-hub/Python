import collections
x=int(input())
lt=[]
for i in range(x):
    lt.append(input())
ans=collections.Counter(lt)
print(len(ans))
for i,j in ans.items():
    print(j,end=' ')
