v=[]
while True :
    M=input()
    if M=="STOP":
        break
    elif M!="STOP":
        v.append(int(M))

V=[] 
for i in v: 
    if i not in V: 
        V.append(i)

for i in V:
    count=0
    for j in range(len(v)):
        if i==v[j]:
            count+=1
    if count>=2 or count<=len(v):
        print(str(i)+"-"+str(count)+" times")
    else:
        print(str(i)+"-"+"1"+" times")