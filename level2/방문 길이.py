def solution(dirs):
    answer = 0
    first_way=[]
    for j in range(21):
        first_way.append([0]*21)#배열 정의
    x=10#처음 x위치
    y=10#처음 y위치
    
    for i in dirs:
        if i=='U': #위쪽으로 한칸가기 'U' 
            if x>0:
                first_way[x-1][y]=1#선 방문한것을 체크
                x-=2#점으로 이동
        elif i=='D': #아래쪽으로 한 칸 가기
            if x<20:
                first_way[x+1][y]=1
                x+=2
        elif i=='R':#오른쪽으로 한 칸 가기
            if y<20:
                first_way[x][y+1]=1
                y+=2
        elif i=='L':#왼쪽으로 한 칸 가기
            if y>0:
                first_way[x][y-1]=1
                y-=2

    for k in range(len(first_way)): #선의 개수 세는 것.
        for j in range(len(first_way)):
            if (k%2==0 and j%2==1)or(k%2==1 and j%2==0):
                if first_way[k][j]==1:
                    answer+=1
    return answer