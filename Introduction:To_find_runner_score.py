n=int(input())
s=input()
list1=[int(item) for item in s.split()]
list1.sort()
for i in range(n-1,-1,-1):
    if(list1[i]!=list1[i-1]):
        print(list1[i-1])
        break
