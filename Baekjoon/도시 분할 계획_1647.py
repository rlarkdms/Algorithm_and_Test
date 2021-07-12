#도시 분할 계획
#동물원의 막 탈출한 원숭이가 세상 구경을 하고 있다.
#마을은 N개의 집과 그 집들을 연결하는 M개의 길로 이루어져 있다.
#길은 어느방향으로든지 다닐 수 있는 편리한 길이다.

# 마을을 2개의 마을로 분리할 예정이다. 

#그럼 지문의 말대로라면 노드가 7개 일 때
# 5개의 선만 필요하다는 뜻이고
# 아마도 신장트리에의 값중에 가장 작은 값을 빼면 된다는 뜻같은데?
import sys
input = sys.stdin.readline
#이렇게 해야 입력값 초과가 안 난다고 한다.

def find_parent(parent,x):
  if parent[x]!=x:
    parent[x]=find_parent(parent,parent[x])
  return parent[x]

def union_parent(parent,a,b):
  a=find_parent(parent,a)
  b=find_parent(parent,b)
  if a<b:
    parent[b]=a
  else:
    parent[a]=b

n,m=map(int,input().split())# n은 집의 개수 m은 길의 개수

parent=[0]*(n+1)

edges=[]
result=0

for i in range(1,n+1):
  parent[i]=i

for i in range(m):
  a,b,cost=map(int,input().split())
  edges.append((cost,a,b))

edges.sort()

count=0
#last=0
for edge in edges:
  cost,a,b=edge
  if find_parent(parent,a)!=find_parent(parent,b):
    count+=1
    union_parent(parent,a,b) #방향성을 설정하는 건데...
    if count==n-1:
      break
    result+=cost
    #last=cost
  
print(result)




