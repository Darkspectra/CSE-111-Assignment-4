s=input()
new=s.split(" ")
n=len(new)
L1=[]
for i in range(n):
    t=int(new[i])
    L1.append(t)
m=input()
new=m.split(" ")
f=len(new)
if f==L1[0]:
    L2=[]
    for k in range(f):
        t=int(new[k])
        L2.append(t)
else:
    print("Wrong Input")

c=0
for i in L2:
    if 0<=i<=5:
        m=L1[1]+i
        if m<L1[0]:
            c+=1
    else:
        print("Wrong input")
a=c//3
if a>=1:
    print(a)
else:
    print(0)