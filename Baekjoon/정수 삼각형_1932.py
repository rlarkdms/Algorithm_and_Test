
N=int(input())
arr=[]
for i in range(N):
    arr.append(list(map(int,input().split())))

for i in range(1,N):
    for j in range(len(arr[i])):
        if j==0:#맨 앞이거나
            arr[i][j]=arr[i][j]+arr[i-1][j]
        elif j==len(arr[i])-1:# 맨뒤면 그냥 위에 있는 값 그대로 가지고 오고
            arr[i][j]+=arr[i-1][j-1]
        else:
            if arr[i-1][j-1]>=arr[i-1][j]:#중간에 있는 값이면 위에 오른쪽과 아래쪽 비교해서 큰 값 가지고 오기.
                arr[i][j]+=arr[i-1][j-1]
            else:
                arr[i][j] += arr[i - 1][j]

print(max(arr[N-1]))

