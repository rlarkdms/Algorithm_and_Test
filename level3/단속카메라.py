def solution(routes):
    #문제를 보니까 감이 잡히는게 왼쪽부터 교집합이 있는지 확인하고 없으면 +1 있으면 그 뒤로 또 교집합 있는지 확인하고 이런식으로 가야하는 것 같음.
    answer = 1
    routes.sort()
    intersection=[-30001,30001]# 교집합을 계산하기 위해 정의
    routes_arr=sorted(routes, key=lambda x:x[0])#정렬

    for i in range(len(routes_arr)):#돌려돌려
        if intersection[0]>routes_arr[i][1] or intersection[1]<routes_arr[i][0]:#교집합이 없는 경우
            intersection=[-30001,30001]#다시 돌아오기 
            answer+=1
        
        #교집합을 정의하기 위한 부분.
        if intersection[0]<=routes_arr[i][0]:
            intersection[0]=routes_arr[i][0]
        if intersection[1]>=routes_arr[i][1]:
            intersection[1]=routes_arr[i][1]
        
    return answer