def fun(arr):#돌면서 뒤집은 값과 똑같은 값이 있는지 확인
    for j in range(n):
        str = list(arr[j])
        str.reverse()
        str=''.join(str)
        for k in range(j,n):
            std=arr[k]
            if std.find(str)!=-1:
                print("%d %c" %(len(str),str[len(str)//2]))
                return 0
n=int(input())

arr=[]
for i in range(n):
    arr.append(input())

arr.sort(key=len)
fun(arr)

