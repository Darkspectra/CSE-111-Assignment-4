p=input("Enter a String: ")
n=''.join(sorted(p))
even, odd, Up, Low = "", "", "", ""
upper, lower,digit = 0, 0,0
for i in range(len(n)): 
    if n[i].isupper():
        Up=Up+n[i]
    elif n[i].islower(): 
        Low=Low+n[i]
    elif n[i].isdigit():
        if int(n[i])%2==0:
            even=even+n[i]
        else:
            odd=odd+n[i]
print(Low+Up+odd+even)