#이문제는 그줄에서 연결된거 있으면 연결된곳으로 가서 싹다 0로 하고 다시하고 하는 거 진행
#그리고 혼자 있는 노드를 위해 노드가 연결이 없으면 그냥 answer+1진행
def solution(n, computers):
    answer = 0
    
    for i in range(n):
        computers[i][i]=0#사실 상 computers[i][j]==1은 필요없는 사항임
        if sum(computers[i])==0:#연결된 곳이 없으면 
            answer+=1#값을 추가
        
    for i in range(n):
        for j in range(n):#돌면서 
            if computers[i][j]==1:#1인 값을 찾고
                answer+=1
                computers=rec(computers,i)#돌면서 0으로 reset시키기
    return answer

def rec(computers,line):
    for j in range(len(computers[line])):
        if computers[line][j]==1:
            computers[line][j]=0#파고들면서 reset
            rec(computers,j)
    else:
        return computers