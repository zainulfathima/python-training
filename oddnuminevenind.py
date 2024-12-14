'''sum of odd nummbers in even indicses'''
l=list(map(int,input().split()))
su=0
for i in range(len(l)):
    if i%2==0:
        if l[i]%2!=0:
            su+=l[i]
print(su)