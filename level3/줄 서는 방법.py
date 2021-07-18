# 생각해보자 일단 순열은 내가알기로 big - O의 시간 복잡도가 2^n 이야 결론은 n이 20까지라면 2^20의 복잡도를 가지게 되는거야...
# 그럼 안돼! 아 아닌가...?
# import itertools

# def solution(n, k):
#     answer = []
#     for i in range(1,n+1):
#         answer.append(i)
#     nPr = list(itertools.permutations(answer, n))
    
#     return list(nPr[k-1])
# 이 방법은 시간 초과가 난다.
# 정보) 코테에서 순열을 써야하는데 범위가 15 넘어가면 가급적 쓰지 말자...

# 이 문제를 푸는 방법은 세션을 나눠서 푸는 방법이다.
# 예시를 가지고 보면
# 1. 미리 line 리스트에 1~n까지의 값을 넣어놓는다.
# 2. k가 5 일때 5를 (n-1)!로 나누고 그럼 2가 나오고 그럼 두번째 세션을 고르고(두번째 세션은 여기서 말하는 3번째인 3으로 시작하는 세션임.)
# 3. 이제 line 리스트에서 그 세션값을 빼서 answer에 넣는다.
# 4. k 값을 (n-1)!의 나머지로 정한다.
# 5. 반복한다. line의 릴스트에 값이 없어질 때까지.
# 이러면 범위가 좁아지면서 값을 고를 수 있다.
import math

def solution(n, k):
    answer=[]
    line=[]
    for i in range(1,n+1):# 1번
        line.append(i)    
    k=k-1 # 이렇게 하는 이유는 값을 처리할 때 1이 시작이 아니라 0을 시작으로 처리했기때문에 k도 거기에 맞춰 -1해줌
    while len(line)!=0:# 5)
        n-=1
        standard_line=math.factorial(n)
        value=k//standard_line # 나눗셈 2)
        
        answer.append(line.pop(value)) #3)
    
        k=k%standard_line # 4)
        
    return answer