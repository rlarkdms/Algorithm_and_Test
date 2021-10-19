#촌수계산
#첫째 줄은 전체 사람의 수 n
#둘째 줄은 촌수를 계산해야 하는 서로 다른 두 사람의 번호가 주어진다.
#셋째 줄에는 부모 자식들 간의 관계의 개수 m이 주어진다.
#넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x,y가 각 줄에 나온다.

#하...이틀째 문제를 계속 풀고 있는데도 문제가 너무 안풀린다... 또 침체기야...ㅠㅠㅜ

n=int(input())
first,last=map(int,input().split())
v=int(input())

# def dfs(graph,v,visted,number,last):
#     visted[v]=True
#     if v==last:
#         return number
#     for i in graph[v]:
#         if not visted[i]:
#             return dfs(graph,i,visted,number+1,last)
#     return -1
INF=987654321
graph=[[INF]*(n+1) for i in range(n+1)]
#visted=[False]*(n+1)
for i in range(n+1):
    graph[i][i]=0
#플로워셜 알고리즘으로 문제 품.
for i in range(v):
    cost=1
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1
#시작노드가 first여야함.
for k in range(n+1):
    for a in range(n+1):
        for b in range(n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

if graph[first][last]==INF:
    print(-1)
else:
    print(graph[first][last])


#print(dfs(arr,first,visted,0,last))

