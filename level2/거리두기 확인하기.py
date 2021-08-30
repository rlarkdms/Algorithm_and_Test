# 각 대기실은 5X5 크기
# 맨허튼 거리가 2이하로 앉아라. 
# 맨허튼 거리란 |r1-r2| + |c1-c2| 이다.

# 예를 들면 판을 기준으로
# (1,1) (1,2) (1,3) (1,4) (1,5)
# (2,1) (2,2) (2,3) (2,4) (2,5)
# (3,1) (3,2) (3,3) (3,4) (3,5)
# (4,1) (4,2) (4,3) (4,4) (4,5)
# (5,1) (5,2) (5,3) (5,4) (5,5)
# 3,3에서 (1)상하좌우는 다 맨하튼 거리를 지키지 않은 경우이고
# (2)두개의 상하좌우의 경우는 파티션이면 지킨 것이고 아니면 지키지 못한 것이다.
# (3)대각선의 경우는 대각선의 가는 길에 빈테이블이 있으면 거리두기를 지키지 않은 것이다.
def solution(places):
    answer = []
    for i in places:
        answer.append(cal(i))
    
    return answer
#P는 사람, O는 빈 테이블, X는 파티션 이다.
def cal(arr):
    x_arr1=[0,0,-1,1] #1)용 x,y 좌표
    y_arr1=[1,-1,0,0]
    x_arr2=[0,0,-2,2] #2)용 x,y 좌표
    y_arr2=[2,-2,0,0]
    x_arr3=[1,1,-1,-1] #3)용 x,y좌표 
    y_arr3=[-1,1,-1,1]
    sum=0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j]=="P":
                for k in range(4):
                    sum+=search_u_d_r_l1(arr,i+x_arr1[k],j+y_arr1[k])#만약 멘하튼 거리를 어기면 1이 나오도록 설정되어있다 그러니 만약 1를 하나라도 더하면
                    sum+=search_u_d_r_l2(arr,i+x_arr2[k],j+y_arr2[k],k)
                    sum+=search_u_d_r_l3(arr,i+x_arr3[k],j+y_arr3[k],k)
        if sum>0:# 멘하튼 거리를 어긴게 된다.
            return 0
    else:
        if sum==0:#어긴게 하나도 없으면 return 1
            return 1
                
def search_u_d_r_l1(arr,x,y):
    if x<0 or y<0 or x>4 or y>4:
        return 0
    if arr[x][y]=='P':#설정된 좌표가 P인 경우는 
        return 1#멘하튼 거리를 어긴것
    else:
        return 0
def search_u_d_r_l2(arr,x,y,k):
    location_arr_x=[0,0,1,-1]
    location_arr_y=[-1,1,0,0]
    if x<0 or y<0 or x>4 or y>4:
        return 0
    if arr[x][y]=='P': #두칸 이동한 좌표는 원점이라 그 사이의 좌표가 X인지만 확인하면 된다.
        if arr[x+location_arr_x[k]][y+location_arr_y[k]]=='X':
            return 0
        else:
            return 1#멘하튼 거리를 어긴것.
    else:
        return 0
def search_u_d_r_l3(arr,x,y,k):
    location_arr_x_1=[-1,-1,1,1]#양쪽을 확인해야해서 이렇게 좌표 설정.
    location_arr_y_1=[0,0,0,0]
    location_arr_x_2=[0,0,0,0]
    location_arr_y_2=[1,-1,1,-1]
    if x<0 or y<0 or x>4 or y>4:
        return 0
    if arr[x][y]=='P':
        if arr[x+location_arr_x_1[k]][y+location_arr_y_1[k]]=='X' and arr[x+location_arr_x_2[k]][y+location_arr_y_2[k]]=='X':
            return 0
        else:
            return 1# 멘하튼 거리를 어긴 것.
    else:
        return 0