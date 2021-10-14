
def solution(n, left, right):
    answer = []    #간단하게 뭐가 들어갈지 생각해보면 됨.
    for i in range(left,right+1):
        if (i%n)>(i//n):#이게 그 후
            answer.append((i%n)+1)
        else:#이게 그 전
            answer.append((i//n)+1)
    return answer