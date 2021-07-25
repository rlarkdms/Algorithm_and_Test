n=int(input())


count=99
for i in range(100,n+1):
    arr=str(i)
    if int(arr[0])-int(arr[1])==int(arr[1])-int(arr[2]):
        count+=1
        
if n<100:
    print(n)

elif n>=100:
    print(count)
    
    
