s1=input()
s2=input()
x1=s1.split(" ")
x2=s2.split(" ")
V=[]
for i in range(len(x1)):
    for j in range(len(x2)):
        V.append(int(x1[i])*int(x2[j]))
print(V)