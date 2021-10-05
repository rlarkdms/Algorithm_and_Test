#타일 채우기.
# 3*N 크기의 벽을 2*1 1*2 크기의 타일로 채우는 경우의 수를 구해보자.
def cal(count):
    arr=[0]*31
    arr[2]=3
    sum_value=0
    for i in range(4,31,2):
        sum_value+=arr[i-4]#사실 이부분이 좀 이해가 안됨...
        arr[i]=arr[i-2]*3+sum_value*2+2
    return arr[count]

n=int(input())

print(cal(n))

