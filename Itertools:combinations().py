from itertools import combinations
s=input()
st=s.split()
lt=[]
word=list(st[0])
word.sort()
w=''.join(word)
for i in range(1,int(st[1])+1):
    com=combinations(w,i)
    for c in com:
        l=''.join(c)
        lt.append(l)
result=sorted(lt,key=len)
for i in result:
    print(i)
