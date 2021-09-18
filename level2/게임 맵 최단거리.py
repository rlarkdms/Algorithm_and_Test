#이게 다익스트라로 풀은건데 이렇게 풀면 착각이 생길 수도 있겠다 되게 애매하다.
import heapq
def solution(maps):
    answer = 0
    #이거 다익스트라이면 금방할듯?
    INF=987654321
    n=len(maps) #세로 길이
    m=len(maps[0]) #가로길이
    #아 조건을 제대로 못봤어... n과 m은 다를 수도 있네...ㅎㅎㅎ...바보인가?
    graph=[[] for _ in range(((n*m)+1))]
    distance=[INF]*((n*m)+1)
    start=1
    
    x_value=[0,1,0,-1]#동남서북
    y_value=[1,0,-1,0]
    for i in range(n):
        for j in range(m):
            if maps[i][j]==1:
                for index in range(4):
                    if i+x_value[index]>=0 and j+y_value[index]>=0 and i+x_value[index]<n and j+y_value[index]<m:
                        if maps[i+x_value[index]][j+y_value[index]]==1:
                        #print((i*n)+(j+1))
                            if index==0:#동
                                graph[(i*m)+(j+1)].append(((i*m)+(j+1)+1,1))
                            elif index==1:#남
                                graph[(i*m)+(j+1)].append((((i+1)*m)+(j+1),1))
                            elif index==2:#서
                                graph[(i*m)+(j+1)].append(((i*m)+(j+1)-1,1))
                            elif index==3:#북
                                graph[(i*m)+(j+1)].append((((i-1)*m)+(j+1),1))

    q=[]
    heapq.heappush(q,(1,start))
    distance[start]=1    
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        
        for i in graph[now]:
            cost=dist+i[1]
            
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
                     
    if distance[n*m]==INF:
        return -1
    else:
        return distance[n*m]
    return answer
