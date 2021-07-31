from itertools import permutations
#내 코드는 효율적이지 못 해ㅠ

N=int(input())

arr=list(map(int,input().split()))

pul,sub,mul,div=map(int,input().split())
expression=[]#expression에 부호를 하나하나 다 넣기
for i in range(pul):
    expression.append('+')
for i in range(sub):
    expression.append('-')
for i in range(mul):
    expression.append('*')
for i in range(div):
    expression.append('/')
#아 생각해보니 +가 여러개면
sort_expression=list(permutations(expression,N-1))# 순열로 구하고

set_expression=list(set(sort_expression))# 이거 안하면 시간초과 남 ㅠ
answer=[]

for j in range(len(set_expression)):#이제 구하기.
    standard=arr[0]
    for i in range(1,len(arr)):
        standard=int(eval(str(standard)+str(set_expression[j][i-1])+str(arr[i])))
    answer.append(standard)

print(max(answer))
print(min(answer))