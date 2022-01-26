# Solved
a=1
b=1
s=0
while(b<=4000000):
    c=a+b
    if(b%2==0):
        s+=b
    a=b
    b=c
print(s)