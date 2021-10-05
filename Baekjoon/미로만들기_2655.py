import sys
import heapq
# 다익스트라 알고리즘
#아 이거보니까 생각한 건데 대각선도 어떻게 구현할지 생각해두는게 좋을 듯.
# 8일 경우
# [0,0] 이런식이 아니라 ->1
# [0,1] 이러식이 아니라 ->2
# [1,0] ->9
#이렇게 정하고 다익스트라 돌리면 값이 distance[n*n]이 나옴.
# 근데 여기서 중요한건
# 지나갈 때 하얀거->하얀으로 갈때는 정삭적인 경로니까 1
# 검정->하얀색 1 하얀색 -> 검정 2500
# 검정->검정 ->2500
#이렇게하면 검정을 밟고 갈 수 있는 최단 경로를 구할 수 있음 추가로 2500으로 설정한 이유는 n*n의 최대값이 2500이기 때문이다.
# 이렇게 distance[n*n]의 최댓값이 나오면 2500이하로 떨어질 때까지 구하면 바꿔야하는 방의 개수를 구할 수 있음!


n=int(input())
INF = 987654321
def fun(n,arr):
    graph = [[] for _ in range((n * n) + 1)]
    distance = [INF] * ((n * n) + 1)
    for i in range(n):#여기서 1~n*n까지 정의하는 부분. 이걸 줄일려면 줄일 수 있는데 귀찮음.. 그냥 노가다가 최고!!
        for j in range(n - 1):
            if arr[i][j] == '1' and arr[i][j + 1] == '1':
                graph[(i * n) + j + 1].append([(i * n) + j + 2, 1])
                graph[(i * n) + j + 2].append([(i * n) + j + 1, 1])

            elif arr[i][j] == '0' and arr[i][j + 1] == '1':
                graph[(i * n) + j + 1].append([(i * n) + j + 2, 1])
                graph[(i * n) + j + 2].append([(i * n) + j + 1, 2500])

            elif arr[i][j] == '1' and arr[i][j + 1] == '0':
                graph[(i * n) + j + 1].append([(i * n) + j + 2, 2500])
                graph[(i * n) + j + 2].append([(i * n) + j + 1, 1])

            elif arr[i][j] == '0' and arr[i][j + 1] == '0':
                graph[(i * n) + j + 1].append([(i * n) + j + 2, 2500])
                graph[(i * n) + j + 2].append([(i * n) + j + 1, 2500])

            if arr[j][i] == '1' and arr[j + 1][i] == '1':
                graph[(j * n) + i + 1].append([((j + 1) * n) + i + 1, 1])
                graph[((j + 1) * n) + i + 1].append([(j * n) + i + 1, 1])

            elif arr[j][i] == '0' and arr[j + 1][i] == '1':
                graph[(j * n) + i + 1].append([((j + 1) * n) + i + 1, 1])
                graph[((j + 1) * n) + i + 1].append([(j * n) + i + 1, 2500])

            elif arr[j][i] == '1' and arr[j + 1][i] == '0':
                graph[(j * n) + i + 1].append([((j + 1) * n) + i + 1, 2500])
                graph[((j + 1) * n) + i + 1].append([(j * n) + i + 1, 1])

            elif arr[j][i] == '0' and arr[j + 1][i] == '0':
                graph[(j * n) + i + 1].append([((j + 1) * n) + i + 1, 2500])
                graph[((j + 1) * n) + i + 1].append([(j * n) + i + 1, 2500])
    start = 1
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])
    count=0
    while True:
        if distance[n * n] < 2500:
            return count
        distance[n * n]-=2500
        count+=1

graph=[[] for _ in range((n*n)+1)]
distance=[INF]*((n*n)+1)
arr=[]
for i in range(n):
    str=input()
    arr.append(list(str))


print(fun(n,arr))
