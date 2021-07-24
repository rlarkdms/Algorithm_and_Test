T=int(input())

n=[0]*11
n[1]=1
n[2]=2
n[3]=4

for i in range(4,11):
    n[i]=n[i-1]+n[i-2]+n[i-3]

for i in range(T):
    k=int(input())
    print(n[k])
    
