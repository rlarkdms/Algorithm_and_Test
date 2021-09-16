#다 돌려야한다는 건데...
#플로워셜 알고리즘 이 문제 플로워셜 알고리즘으로 구현하고 처음 위치에서 1~N+1까지 돌린 다음 나온위치에서 a랑 b까지의 거리를 구하면 됨.
#근데 아무리봐도 이런식으로 푸는 문제가 아니었을 것 같음 이렇게 푸는 거 치고 시간복잡도가 너무 큼...
def solution(n, s, a, b, fares):
    answer = 987654321
    INF=987654321
    
    graph_fl=[[INF]*(n+1) for _ in range(n+1)]
    
    graph_fl=vmf(graph_fl,n,fares)
    
    for i in range(1,n+1):

        answer=min(answer,graph_fl[s][i]+graph_fl[i][a]+graph_fl[i][b])#제일 작은걸 골라내는 과정.

    return answer

def vmf(graph,n,fares):#플로워셜 알고리즘 구현.
    
    for i in range(n+1):
        graph[i][i]=0
    
    for i in fares:
        graph[i[0]][i[1]]=i[2]
        graph[i[1]][i[0]]=i[2]
        
    for k in range(n+1):
        for a in range(n+1):
            for b in range(n+1):
                graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])
    
    return graph