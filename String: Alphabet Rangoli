def print_rangoli(size):
    arr=[]
    dash=((size-1)*2)
    for i in range(1,size+1):
        str1=''
        str1+='-'*dash
        for j in range(size,size-i,-1):
            if(j==(size-i-1) or i==1):
                str1+=chr(96+j)
            else:
                str1=str1+chr(96+j)+'-'
        for k in range(j+1,size+1):
            if(k==size or i==1):
                str1+=chr(96+k)
            else:
                str1=str1+chr(96+k)+'-'
        str1+='-'*dash
        dash-=2
        print(str1)
        arr.append(str1)
    arr.pop()
    for i in reversed(arr):
        print(i)
            
        
        

