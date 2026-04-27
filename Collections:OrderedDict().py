from collections import OrderedDict
n=int(input())
dic=OrderedDict()
for i in range(n):
    cm=''
    cm=input().rsplit(maxsplit=1)
    if(cm[0] in dic):
        val=0
        val=dic[cm[0]]
        dic[cm[0]]=str(int(val)+int(cm[1]))
    else:
        dic[cm[0]]=cm[1]
for key, value in dic.items():
    print(f"{key} {value}")
        
    
