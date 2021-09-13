from collections import deque
import sys

def cal(arr):#함수
    answer=0#개수 세기.
    q=deque()#큐 선언
    x_len=len(arr) #X의 길이
    y_len=len(arr[0])# Y의 길이
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j]==1:#만약 1이면==섬이면
                answer+=1#하나 더하고 이제 돌려돌려 돌림판 BFS로 간다.
                q.append([i,j])#이게 갑을 하나 넣고
            while q:#큐의 값이 없어질 때까지 돌기

                a,b=q.popleft()#앞에 값을 빼고
                arr[a][b]=0
                x_value=[-1,1,-1,1,0,0,1,-1]#상하좌우 대각선 다 탐색하기 위해 필요
                y_value=[-1,1,1,-1,1,-1,0,0]
                for index in range(8):
                    #print(a + x_value[index], b + y_value[index])
                    #print(i,j)
                    if (a+x_value[index])>=0 and (b+y_value[index])>=0 and (a+x_value[index])<x_len and (b+y_value[index])<y_len:
                        #print(a+x_value[index],b+y_value[index])
                        if arr[a+x_value[index]][b+y_value[index]]==1:#만약 상하좌우대각선중 1이 있으면 큐에 넣어두기
                            #print("들어옴")
                            q.append([a+x_value[index],b+y_value[index]])# 큐에 넣는 부분.
                            arr[a+x_value[index]][b+y_value[index]]=0#저기 위에서만 셋해주면 속도가 느림.
    return answer#이제 값을 얻을 수 있음.
while True:#여기서는 값 받는 부분
    w,h=map(int,sys.stdin.readline().split())
    if w==0 and h==0:
        break
    #arr=[[]*w for _ in range(h)]
    arr=[]
    for i in range(h):#이차원 배열 받기
        arr.append(list(map(int,sys.stdin.readline().split())))

    print(cal(arr))#함수 돌리기






