def solution(x, n):
    answer = []
    if x==0:#0만 따로 해결
        for i in range(n):
            answer.append(0)#배열에 넣고
    else:# 
        for i in range(x,x*(n+1),x): #x는 x*(n+1)까지 x배 만큼 올라감.
            answer.append(i)#배열에 넣고
    return answer