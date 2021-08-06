def solution(N, road, K):
    answer = 0
    #이 문제는 전형적인 플로워셜 알고리즘 문제.
    graph=[[987654321]*(N+1) for j in range(N+1)]

    for i in range(1,N+1):
        for j in range(1,N+1):
            if i==j:
                graph[i][j]=0
                
    road_sort=sorted(road, key=lambda x:x[2], reverse=True)#이게 있는 이유는 문제 보면 같은 경로에 여러개의 값이 주어졌을 수 있는데 최단거리를 구해야하는 거기 때문에 값 넣을 때 뒤에가 작은 값이 가도록해야함.
    
    for i in road_sort:
        graph[i[0]][i[1]]=i[2]
        graph[i[1]][i[0]]=i[2]
    
    for k in range(1,N+1):
        for a in range(1,N+1):
            for b in range(1,N+1):
                graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

    for i in range(1,N+1):
        if graph[1][i]<=K:# 1에서 가는것중에 K보다 작은 값을 구하기.
            answer+=1
    
    return answer