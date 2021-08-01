#안테나
#일직선에 여러 채가 있다.
#이중에서 특정 위치의 집에 특별히 한 개의 안테나를 설치하기 위해
# 이 문제는 규칙을 알면 풀 수 있는 문제였음.
# 0 4 6 8
# 4 0 2 4
# 6 2 0 2
# 8 4 2 0
# 이런식으로 앞에꺼 뺴기 뒤에꺼를 일렬로 돌면서 

N=int(input())

arr=list(map(int,input().split()))

arr.sort()
sum_value=[]

value=0

for i in range(1,len(arr)):
    value+=(arr[i]-arr[0])

sum_value.append([value,arr[0]])

length=len(arr)

standard=0

for j in range(length-1):
    standard=arr[j+1]-arr[j]# 그 값
    sum_value.append([sum_value[j][0]+((standard*(j+1))-(standard*(length-j-1))),arr[j+1]])

print(min(sum_value)[1])
