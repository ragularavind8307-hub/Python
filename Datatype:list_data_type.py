def menuf(b):
    a=[int(item) if(item.isdigit()) else item for item in b]
    if(a[0]=="insert"):
        list1.insert(a[1],a[2])
    elif(a[0]=="print"):
        print(list1)
    elif(a[0]=="remove"):
        list1.remove(a[1])
    elif(a[0]=="append"):
        list1.append(a[1])
    elif(a[0]=="sort"):
        list1.sort()
    elif(a[0]=="pop"):
        list1.pop()
    elif(a[0]=="reverse"):
        list1.reverse() 
n=int(input())
menu=["insert","print","remove","append","sort","pop","reverse"]
list1=[]
arr=[]
for i in range(0,n):
    x=input()
    arr=x.split()
    menuf(arr)
