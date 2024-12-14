n=int(input("enter the number u wannna check "))
count=0
for i in range(1,n+1):
    if sum%i==0:
        count+=1
if count<=2:
    print("hell yeah its a fucking prime dude")
else:
    print("sadly its not a prime rn")





''' another way for prime uaing break and flag
n=int(input())
flag=0
for i in range(2,n):
    if n%i==0:
        flag=1
        break
if flag==0:
    print("prime")
else:
    print("not prime")'''