'''
arr=list(map(int,input().split()))
new_arr=[]
for i in arr:
    if i%3!=0 and i%10!=3:
        new_arr.append(i)
print(new_arr)
'''
n=int(input())
arr=[]
for _ in range(n):
    k=int(input())
    
    i=1
    count=0
    while(1):
        if i%3!=0 and i%10!=3:
            count+=1
            if count==k:
                arr.append(k)
                break
        i+=1
print(arr)
    