d=[-1]*1000001

n=int(input())
d[1]=0
d[2]=1
d[3]=1
d[4]=2
d[5]=3

a=0
for i in range(6,n+1): #생각해보니 가장 적은걸 고르면 되잖아
  min_val=10000001

  if i%3==0:
    a=int(i/3)
    if min_val>=d[a]:
      min_val=d[a]
    a=0
  if i%2==0:
    a=int(i/2)
    if min_val>=d[a]:
      min_val=d[a]
    a=0
  a=i-1
  if min_val>=d[a]:
    min_val=d[a]
  
  d[i]=min_val+1

print(d[n])