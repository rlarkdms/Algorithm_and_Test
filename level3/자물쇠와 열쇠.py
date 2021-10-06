def solution(key, lock):
    #그냥 다 정해놓고 하면 안되나? 그것도 속도가 느리진 않을 텐데?
    key_len=len(key)
    lock_len=len(lock)
    len_sen=lock_len+(key_len-1)*2
    arr=[]
    #홈이 몇개인지 세기위한 부분
    standard=0
    for a in range(lock_len):
        for b in range(lock_len):
            if lock[a][b]==0:
                standard+=1
                
                
    #이 부분이
    # LOCK이 이라면 밑에 루틴을 통해 
    # 1 1 1      2 2 2 2 2 2 2
    # 1 1 0      2 2 2 2 2 2 2
    # 1 0 1      2 2 1 1 1 2 2 
                #2 2 1 1 0 2 2
        #        2 2 1 0 1 2 2
        #        2 2 2 2 2 2 2
        #        2 2 2 2 2 2 2 
    #이렇게 변경한뒤 0,0 부터 4,4까지 비교하면서 돌기.
    for i in range(len_sen):#이게 그 앞에 넣을 배열
        arr.append(2)
    for i in range(lock_len):
        for j in range(key_len-1):
            lock[i].insert(0,2)
            lock[i].append(2)
    
    for k in range(key_len-1):
        lock.insert(0,arr)
        lock.append(arr)
    # 선언부 인데 연산을 편하게 하기 위해서 
    # 배열에 위 아래 왼쪽 아래에 값들을 넣어서 돌림.
    #---------------------------------------------------
    # 계산부
    
    for k in range(4):#돌리기 위해
        for i in range(len(lock)-key_len):#배열기준점을 움직이기 위해 i,j 사용
            for j in range(len(lock)-key_len):
                value=standard
                for a in range(key_len):#그 기준점에 따른 배열에서 돌리기 위해 사용.
                    for b in range(key_len):
                        if lock[i+a][j+b]==1:#돌기랑 돌기랑 닿으면 안된다라는 조건을 만족하기 위한
                            if key[a][b]==1:
                                break
                        if lock[i+a][j+b]==0:#이건 key랑 lock이랑 만나면 열수 있다는 조건.
                            if key[a][b]==1:
                                value-=1
                else:
                    if value==0:#돌기랑 돌기랑 만나지 않고 key lock이 만나는 경우에는 True
                        return True
        key=rotated(key)#돌리기.
        
    return False#아닌 경우에는 삐꾸
def rotated(a):#이건 그냥 인터넷 보고 배낌. 행렬 회전 시키기.
    n = len(a)
    m = len(a[0])

    result = [[0]* n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result