n=int(input("enter evennts:"))
events=list(map(int,input().split()))
count=0
police=0
untreated_crimes=0
for i in events:
    if i<0:
        count+=1
        untreated_crimes=count-police
    elif i>0:
        police+=i
print(untreated_crimes)

'''
after n
unsolved=0
police=0
event=list(map(int,input().split()))
for e in event:
    if e==-1:
        if police>0:
            police=-1
        else:
            unsolved+=1
    else:
        police+=e
print(unsolved)'''