#이문제는 배열을 만들어서 배열마다 갈 수 있는 값을 넣으면 될 것 같은데...
def solution(m, n, puddles):
    answer=0
    INF=987654321
    graph=[[0]*(m+1) for _ in range(n+1)]
    graph[1][0]=1
    for i in puddles:
        graph[i[1]][i[0]]=INF
    
    for i in range(1,n+1):#탐색하면서 돌기
        for j in range(1,m+1):
            if graph[i][j]!=INF:
                if graph[i-1][j]==INF and graph[i][j-1]!=INF:#만약 위가 웅덩이 일떄 왼쪽껏만 더하기
                    graph[i][j]=graph[i][j-1]%1000000007
                elif graph[i-1][j]!=INF and graph[i][j-1]==INF:#만약 왼쪽이 웅덩이 일때 왼쪽껏만 더하기.
                    graph[i][j]=graph[i-1][j]%1000000007
                elif graph[i-1][j]!=INF and graph[i][j-1]!=INF:#만약 왼쪽과 위쪽이 웅덩이가 아닐때 왼쪽과 위 둘 다 더하기.
                    graph[i][j]=(graph[i-1][j]+graph[i][j-1])%1000000007 #조건에 1000000007로 나눠라라는게 있기 때문에 나누기.
                #여기서 위와 왼쪽이 웅덩이 일 경우는 안 넣어도 되는게 해당되는게 없으니까 아무런 이벤트 없이 지나가니까 문제가 없다.

    return graph[n][m]
#근데 이해가 안되는게 왜 좌표가 거꾸로지...?