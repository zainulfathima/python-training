li=[1,2,3,1,2,3,4,9,2,7,3,6,8,2,9]
c=[]
for i in li:
    if li.count(i)%2!=0 and li[i] not in c:
        c.append(li[i])
print(c)
# for i not 