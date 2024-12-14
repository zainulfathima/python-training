inp=int(input("enter duh!"))  #accenture
i = inp
count=0
while(i!=0):
    if i%5==0:
        i-=5
        count+=1
    elif i%5!=0:
        rest=i%5
        count+=1
        i-=rest
else:
    print()
print(count)
