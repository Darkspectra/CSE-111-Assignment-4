s=input()
new=s.split(",")
n=len(new)
L1=[]
for i in range(n):
    t=int(new[i])
    L1.append(t)
    
m=input()
new=m.split(",")
f=len(new)
L2=[]
for k in range(f):
    t=int(new[k])
    L2.append(t)

L1[-1:]=L2
print(L1)