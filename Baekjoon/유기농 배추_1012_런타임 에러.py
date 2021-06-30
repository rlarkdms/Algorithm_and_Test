def dfs(x,y,a,b):
    global arr
    

    
    if x>a or x<0 or y>b or y<0:
        
        return 0
    #print("X %d y %d" %(x,y))
    arr[x][y]=0
    
    if arr[x+1][y]==1:
        dfs(x+1,y,a,b)

    if arr[x][y+1]==1:
        dfs(x,y+1,a,b)

    if arr[x-1][y]==1:
        dfs(x-1,y,a,b)
        
    if arr[x][y-1]==1:
        dfs(x,y-1,a,b)    

n=int(input())

global arr
arr=[]

for i in range(n):
    num=0
    arr=[]
    a,b,c=map(int,input().split())
    
    for j in range(a+1):
        arr.append([0]*(b+1))#배열 정의
    for j in range(c):
        n1,n2=map(int,input().split())
        arr[n1][n2]=1

    for i in range(a):
        for j in range(b):
            if arr[i][j]==1:
                dfs(i,j,a,b)
                num+=1
    print(num)



