while True:
    N=input()
    if N=="STOP":
        break
    else:
        J=True
        new=N.split(" ")
        L=len(new)
        L1=[]
        for i in range(L):
            t=int(new[i])
            L1.append(t)
        L2=[]
        for i in range(L-1):       # INPUT=[1, 4, 2, 3],,,then the for loop value would be (1,4,2)
            a=abs(L1[i+1]-L1[i]) # (L-1) checking for jolly pattern AND (abs) is for turning to absolute value
            L2.append(a)
        L2.sort()
        for i in range(L-1):
            if L2[i]!=i+1:
                J=False
        if J==False:
            print("Not UB Jumper")
        else:
            print("UB Jumper")