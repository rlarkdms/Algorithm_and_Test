import itertools

N,M=map(int,input().split())

arr=list(map(int,input().split()))


answer=list(itertools.combinations(arr,3))

sort_arr=[]

for i in answer:
    sort_arr.append(sum(i))
sort_arr.sort()
output=0
for i in sort_arr:#가다가 M를 넘기면 그 전값을 고르고 M를 넘기는 값이 없으면 그냥 return
    if i>M:
        break
    else:
        output=i

print(output)
