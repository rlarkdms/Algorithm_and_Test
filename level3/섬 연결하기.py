def solution(n, costs):
    # 이건 그리디 문제가 아님;;
    # 최소신장트리 문제임 노드 연결이 n-1
    # 이건 크루스칼 알고리즘으로 인해 한줄로 연결된 선을 구할 수 있음.
    parent=[0]*(n+1)

    edges=[]
    result=0

    for i in range(1,n+1):#parent 정의를 하고
        parent[i]=i

    for i in costs:# 비용과 간선들 정보를 얻기.
        edges.append((i[2],i[0],i[1]))

    edges.sort()#작은 순서대로 정렬

    for edge in edges:#이게 돌면서 가장 작은거 부터 순서대로 삽입하면서 가는 것.
        cost,a,b=edge
        if find_parent(parent,a)!=find_parent(parent,b):#이게 순환이 아니면 이란 뜻.
            union_parent(parent,a,b)
            result+=cost#최소 비용 합하기

    return result

#이 밑에 두부분이 집합을 찾는 과정이긴 한데...
def find_parent(parent,x):#부모 노드를 찾는 과정.
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):#유니온 이게 더작은 값으로 정의하는 것.
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b