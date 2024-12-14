inp=str(input())
sum=0
for i in inp:
    sum+=int(i)
print(sum)
count=0
for i in range(1,sum+1):
    if sum%i==0:
        count+=1
if count<=2:
    print("googly")
else:
    print("not googly")