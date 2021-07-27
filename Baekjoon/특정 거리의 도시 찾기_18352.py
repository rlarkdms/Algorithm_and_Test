from collections import deque
# N -> 도시의 개수, M -> 도로의 개수, K -> 거리의 정보, X -> 출발 도시
import sys
N,M,K,X=map(int,sys.stdin.readline().split())#이거때문에 엄청 헤맸네 입력값이 많을 때에는 input() -> sys.stdin.readline()
visted=[0]*(N+1)
graph=[[] for i in range(N+1)]
for i in range(M):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)#이 graph의 꺼를 다 써야해...!
#아 그래 graph에 이렇게 넣는게 아니였어
#시작이 X란 말이야 이걸 잘 정해야함.
answer=[]
def bfs(x,dist):
    q=deque()#큐 생성
    q.append([x,dist])#노드랑 거리 넣기
    visted[1]=1#이거 없으니까 순환에서 문제가 생김
    while q:
        a,di=q.popleft()#큐에서 값 빼고
        if di==K:#맞는 값 나오면 리스트에 넣고
            answer.append(a)

        for i in graph[a]:# 뒤에서 돌기
            if visted[i]==0:#만약 들린 곳이 아니면
                visted[i] = 1# 들린곳으로 표시
                q.append([i,di+1])#그 다음 넣기

    return 0
bfs(X,0)

answer.sort()# 오름차순으로 넣어야 해서 sort
if len(answer)==0:
    print(-1)
else:
    for i in answer:
        print(i)