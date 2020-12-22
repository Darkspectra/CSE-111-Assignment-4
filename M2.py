def Sum(list1):
    m = 0
    for x in list1: 
        m = max(sum(x), m)
    for i in list1:
        if sum(i)==m:
            print(m)
            print(i)

N=int(input())
L2=[]
for i in range(N):
    s=input()
    new=s.split(" ")
    n=len(new)
    L1=[]
    for i in range(n):
        t=int(new[i])
        L1.append(t)
    L2.append(L1)
Sum(L2)