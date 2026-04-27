def minion_game(st):
    stuart=0
    kevin=0
    vow=['A','E','I','O','U']
    n=len(st)
    for i in range(len(st)):
            if(st[i] in vow):
                kevin+=n-i
            else:
                stuart+=n-i
    if(kevin<stuart):
        print("Stuart",stuart)
    elif(kevin==stuart):
        print("Draw")
    else:
        print("Kevin",kevin)

