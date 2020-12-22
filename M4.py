
# WITHOUT SLICING
'''n=int(input())
s=input()
L2=[]
i=0
while i<n:
    j=i
    L1=[]
    while j<len(s):
        L1.append(s[j])
        j=j+n
    L2.append(L1)
    i=i+1
print(L2)'''

# WITH SLICING
N=int(input())
S=input()
Sl_ice=S.split(", ")

L1=[]
for i in range(N):
    L1.append(Sl_ice[i::3])
print(L1)