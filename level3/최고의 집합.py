def solution(n, s):
    # 곱하기는 숫자들의 크기가 차이가 안날때가 가장 이상적이게 됨.
    # 이 문제는 굉장히 간단한 문제로 말그대로 숫자의 크기 차이가 얼마 안나야함
    answer = []
    k=s//n#그래서 나눗셈과
    m=s%n#나머지를 통해서 몇개가 1를 더해야하는지 알아내고 알아낸 값만큼 append해주는거임.
    if k==0:
        answer.append(-1)
        return answer
    
    for i in range(0,n-m):
        answer.append(k)
    for j in range(n-m,n):
        answer.append(k+1)
    
    return answer