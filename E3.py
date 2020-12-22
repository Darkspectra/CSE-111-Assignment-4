# THIS FUCKING SET

'''v=[]
l=10
for i in range(l):
    M=int(input("Enter a number: "))
    v.append(M)
    if len(v) != len(set(v)):
        print("Enter a different number")
        l=l+10
        v[i]=l'''

# THIS TIME MY BRAIN WORKS
L = []
m=int(input())
L.append(m)
n=1
while n<10:
    m=int(input())
    C=0
    for j in range(len(L)):
        if L[j]==m:
            C+=1
    if C>=1:
        print("Duplicate found!!")
    else:
        L.append(m)
        n+=1