from itertools import groupby
s=input()
st=groupby(s)
for i,j in st:
    print((len(list(j)),int(i)),end=' ')
