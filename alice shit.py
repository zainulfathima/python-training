''' alice climbs a staircase and takes N steps to reach the top . 
In each turn alice can climb 1 or M stairs. find the minimum number of climbs to reach the top i.e Nth stair'''
n,m=map(int,input().split())
if n<m:
    print(1)
elif n%m==0:
    print(n//m)
else:
    print((n//m)+(n/m))