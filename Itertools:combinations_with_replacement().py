from itertools import combinations_with_replacement
s=input().split()
st=''.join(sorted(s[0]))
com=combinations_with_replacement(st,int(s[1]))
for i in com:
    print(''.join(i))
