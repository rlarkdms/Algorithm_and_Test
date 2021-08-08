#퇴사 할 때 받을 수 있는 최고의 금액을 골라보자
# 3일뒤에 상담을 받을 수 있다고 하면 상담 받을 수 있는 날짜 뒤에 날짜에 고를 수 있게 배열에 넣어두겠어

N=int(input())

arr=[]
for i in range(N):
    t,p=map(int,input().split())
    arr.append([t,p])

dp_arr=[[0] for j in range(20)]#이게 사실은 15+5까지 값을 여기까지 받을 수 있어서

#입력단

for j in range(len(arr)):
    arr[j][1]=arr[j][1]+max(dp_arr[j + 1]) #그 배열에 넣은 곳중에 가장 큰 값을 더하기.
    for k in range(arr[j][0]+1+j,20):#여기가 위에서 말한것 처럼 상담을 받을 수 있다고 한 날 뒤부터 배열에 넣어두는 거
        dp_arr[k].append(arr[j][1])#그래서 배열에 넣는 부분

max_value=0
for index in range(N-1,-1,-1):#이게 그래서 결정된 값중에 가장 큰 값 넣는 부분.
    if arr[index][0]+index<=N:
        if max_value<arr[index][1]:
            max_value=arr[index][1]
print(max_value)





