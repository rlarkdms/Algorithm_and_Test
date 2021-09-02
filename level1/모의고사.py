# 이 문제 내가 계속 못 풀고 있던 문제였는데 속이 시원하다!
def solution(answers):
    answer = []
    value=[0,0,0]
    A=[0]
    B=[0]
    C=[0]
    for i in range(2500):
        A.append(1)
        A.append(2)
        A.append(3)
        A.append(4)
        A.append(5)
    for i in range(1250):
        B.append(2)
        B.append(1)
        B.append(2)
        B.append(3)
        B.append(2)
        B.append(4)
        B.append(2)
        B.append(5)
    for i in range(1000):
        C.append(3)
        C.append(3)
        C.append(1)
        C.append(1)
        C.append(2)
        C.append(2)
        C.append(4)
        C.append(4)
        C.append(5)
        C.append(5)
    
    for j in range(len(answers)):
        if answers[j]==A[j+1]:
            value[0]+=1
        if answers[j]==B[j+1]:
            value[1]+=1
        if answers[j]==C[j+1]:
            value[2]+=1
    
    
    for i in range(3):
        if value[i]==max(value):
            answer.append(i+1)
    return answer