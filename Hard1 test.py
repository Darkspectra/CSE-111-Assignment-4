def isJolly(a, n): 
    diffSet = [False] * n   
    for i in range(n):
        d = abs(a[i]-a[i + 1]) 
        if (d == 0 or d > n-1 or diffSet[d] == True): 
            return False 
        diffSet[d] = True  
    return True


while True:
    s=input()
    if s=="STOP":
        break
    else:
        jolly=True
        new=s.split(" ")
        n=len(new)
        L1=[]
        for i in range(n):
            t=int(new[i])
            L1.append(t)
    V=L1
    N=len(V)
    if isJolly(V, N):
        print("UB Jumper")
    else:
        print("Not UB Jumper")