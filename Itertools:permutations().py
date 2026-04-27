from itertools import permutations
s=input()
st=s.split()
lt=[]
pre=permutations(st[0],int(st[1]))
for p in pre:
    m=''.join(p)
    lt.append(m)
lt.sort()
for i in lt:
    print(i)
