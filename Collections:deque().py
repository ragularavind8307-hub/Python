from collections import deque
x=int(input())
d=deque()
for i in range(x):
    st=input().split()
    if(st[0]=='append'):
        d.append(int(st[1]))
    elif(st[0]=='appendleft'):
        d.appendleft(int(st[1]))
    elif(st[0]=='pop'):
        d.pop()
    elif(st[0]=='popleft'):
        d.popleft()
print(*d)
