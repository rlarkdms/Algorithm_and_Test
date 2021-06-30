n,k=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(int(input()))
sum=0
for i in range(n-1,-1,-1):
    sum=sum+(k//arr[i])
    k=k%arr[i]

print(sum)
