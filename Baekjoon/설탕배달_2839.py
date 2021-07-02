n=int(input())

arr=[-1]*5001

arr[3]=1
arr[5]=1
for i in range(6,5001):
    a=5000
    b=5000
    if arr[i-3]!=-1:
        a=arr[i-3]

    if arr[i-5]!=-1:
        b=arr[i-5]
    if a==5000 and b==5000:
        continue
    if a>b:
        arr[i]=b+1
    else:
        arr[i]=a+1

print(arr[n])
