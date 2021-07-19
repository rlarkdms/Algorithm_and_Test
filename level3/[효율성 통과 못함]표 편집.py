from collections import deque
#이문제가 그때 못 풀었던 문제
# "U X"는 현재 위에 행을 선택
# "D X"는 현재 아래에 있는 행을 선택
# "C" 현재의 행을 삭제 후 바로 아래 행 선택, 삭제된 행이 마지막 행인 경우는 바로 윗행 선택
# "Z" 가장 최근에 삭제된 행을 원래대로 복구합니다.

#아 내가 왜 이 문제에 예외사항을 극복 못했는지 드디어 알았다.내가 잘못생각하고 있던것 중에하나가
# X가 한자리수가 아닐 수 있다 234이럴수도 있는데 이걸 고려 못했다....
# 이 문제 거의 구현 문제인데 구현에서는 유연한 사고가 필요한데 선입견에 잡혀있었네...멍청아 제발...선입견을 가지지마.
def solution(n, k, cmd):
    answer = ''
    arr_del=[]#뒤로 가기를 위한것
    
    arr_real=deque()
    arr_real=[i for i in range(n)]
    for i in cmd:
        # print("k값: %d" %k)
        # print(arr_del)
        if i[0]=='U':
            k-=int(i[2:])
            #여기서 그 상황도 만들어야지
        elif i[0]=='D':
            k+=int(i[2:])
        elif i[0]=='C':
            a=arr_real[k]#a는 값을 가지고 있어야 함.
            arr_real.pop(k)#여기가 가장 문제임 시간 복잡도에 
            arr_del.append([k,a])#k는 위치고 
            if k==len(arr_real):
                k-=1
        elif i[0]=='Z':
            value=arr_del.pop()
            arr_real.insert(value[0],value[1])
            if value[0]<=k:
                k+=1
  
    
    for i in range(n):
        if i in arr_real:
            answer+='O'
        else:
            answer+='X'
        
    return answer