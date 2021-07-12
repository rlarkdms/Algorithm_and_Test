import heapq

def solution(n, edge):#다익스트라 알고리즘 이용하는 문제
    answer = 0
    INF=987654321
    start=1
    
    graph=[[] for i in range(n+1)]# 그래프 정의
    distance=[INF]*(n+1)#거리 정의
    
    for i in edge:
        graph[i[0]].append((i[1],1))#방향성이 없으니까 둘 다 정의
        graph[i[1]].append((i[0],1))
    
    q=[]
    heapq.heappush(q,(0,start))#값 넣고
    distance[start]=0
    
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        
        for i in graph[now]:
            cost=dist+i[1]
            
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    value=0
    for i in range(1,n+1):#루틴을 돌면서
        if distance[i]==INF:
            print("INF")
        else:
            value=max(distance[i],value)#가장 큰 값을 찾고
    
    
    return distance.count(value)#가장 큰 값 카운트하기

                
                