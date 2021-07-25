N=int(input())

arr1=list(map(int,input().split()))
#계수정렬로 해결하자
plus=[0]*10000000
sub=[0]*10000000


for i in arr1:
    if i>=0:
        plus[i]=1
    else:
        sub[i]=1


M=int(input())

answer=[]

arr2=list(map(int,input().split()))

for i in arr2:
    if i>=0:
        if plus[i]==1:
            answer.append(1)

        else:
            answer.append(0)

    else:
        if sub[i]==1:
            answer.append(1)

        else:
            
            answer.append(0)

for i in answer:
    print(i, end=" ")
