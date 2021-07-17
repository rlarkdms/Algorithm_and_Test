#기둥은 바닥 위에 있거나 보의 한쪽 끝 부분에 있거나 다른 기둥 위에 있어야 한다.
#보는 한쪽 끝 부분이 기둥 위에 있거나,또는 양쪽 끝 부분이 다른 보와 동시에 연결 되어 있어야 합니다.
#문제가 너무 긴데;
# [x,y,a,b] -> x,y는 a에서 0은 기둥, 1은 보 b에서 0은 삭제 1은 설치
# 보는 오른쪽으로 설치, 기둥은 위 방향으로 설치
from operator import itemgetter

def solution(n, build_frame):
    answer = [[]]
    result=[]
    space_pillar=[]
    space_bo=[]
    for i in range(n+1):
        space_pillar.append([-1]*(n+1))
        space_bo.append([-1]*(n+1))
    
    
    for index in build_frame:
        #아 여기서 조건이 들어가야 하는 구나!

        
        if index[3]==1 and index[2]==0:#설치이면 기둥
            #바닥이랑 연결되어 있거나 보 위에 있거나 다른 기둥 위에 있어야함.
            if index[1]==0 or space_pillar[index[1]-1][index[0]]==1 or space_bo[index[1]][index[0]-1]==1: 
                space_pillar[index[1]][index[0]]=1
                
                
                
        elif index[3]==1 and index[2]==1:#설치이고 보
            #보는 한쪽 끝 부분이 기둥위에 있거나 아니면 양쪽 끝 부분이 보와 연결되어있어야함.
            #print(index[1])
            #print(index[0])
            if space_pillar[index[1]-1][index[0]]==1 or space_pillar[index[1]-1][index[0]+1] ==1 or (space_bo[index[1]][index[0]+1]==1 and space_bo[index[1]][index[0]-1]==1):  
            
                space_bo[index[1]][index[0]]=1
        elif index[3]==0 and index[2]==0:#삭제이면 기둥
            #삭제도 조건에 따라야 한다는 거겠지?
            #삭제가 안되는 조건을 생각해보자.
            #삭제가 되는 경우는 두쪽 다 있을 경우만 삭제 가능하고
            if space_bo[index[1]+1][index[0]]==1 and space_bo[index[1]+1][index[0]+1]==1:
            
                space_pillar[index[1]][index[0]]=-1
        
        elif index[3]==0 and index[2]==1:#삭제이고 보이면 #이 경우는 주변에 기둥이 없고 양쪽에 보가 있을 경우
            if (space_bo[index[1]][index[0]+1]==1 and space_bo[index[1]][index[0]-1]==1) and (space_pillar[index[1]-1][index[0]]==-1 or space_pillar[index[1]-1][index[0]+1] ==-1):
                pass
            else:
                space_bo[index[1]][index[0]]=-1

        # print("기둥")
        # for i in space_pillar:
        #     print(i)
        # print("보")    
        # for j in space_bo:
        #     print(j)            
            
            
    for i in range(n+1):
        for j in range(n+1):
            rep=[]
            if space_pillar[i][j]==1:
                rep.append(j)
                rep.append(i)
                rep.append(0)
                result.append(rep)
    for i in range(n+1):
        for j in range(n+1):
            rep=[]
            if space_bo[i][j]==1:
                rep.append(j)
                rep.append(i)
                rep.append(1)
                result.append(rep)
    
    result.sort(key=itemgetter(0,1,2))
    print(result)
    return result