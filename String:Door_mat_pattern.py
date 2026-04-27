r=input()
arr=[int(item) for item in r.split()]
row=arr[0]//2
dash=(arr[1]//2)-1
rev=[]
for i in range(1,row+1):
    str1=''
    str1+='-'*dash
    str1+='.'
    for j in range(1,i*2):
        if(j!=(i*2)):
            str1+='|'
        if(j!=(i*2)-1):
            str1+='..'
    str1+='.'
    str1+='-'*dash
    dash-=3
    print(str1)
    rev.append(str1)
wel=(arr[1]-7)//2
str1=print('-'*wel+'WELCOME'+'-'*wel)
for i in reversed(rev):
    print(i)
    
