from collections import deque
n,m=map(int,input().split())
arr=[]
for i in range(n):
    long_int=input()
    str=[]
    for j in range(m):
        str.append(int(long_int[j]))
    arr.append(str)

q=deque()
visted=[] #방문 가중치

for k in range(n):
    sentence=[]
    for index in range(m):
        sentence.append(0)
    visted.append(sentence)

q.append([0,0])
visted[0][0]=1
while q:
    a,b=q.popleft()
    x_value=[-1,0,1,0]#북 동 남 서
    y_value=[0,1,0,-1]
    for i in range(4):
        if (a+x_value[i])>=0 and (b+y_value[i])>=0 and (a+x_value[i])<n and (b+y_value[i])<m:
            #print(a+x_value[i],b+y_value[i])
            #print(arr)
            if arr[a+x_value[i]][b+y_value[i]]==1:
                q.append([a+x_value[i],b+y_value[i]])
                arr[a+x_value[i]][b+y_value[i]]=2
                visted[a+x_value[i]][b+y_value[i]]=max(visted[a+x_value[i]][b+y_value[i]],visted[a][b]+1)

print(visted[n-1][m-1])
