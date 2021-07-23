#stack 이랑 queue같이 써야한다.
from collections import deque
def solution(s):
    answer = 0
    q=deque()
    for i in s:#큐에 값을 집어넣기.
        q.append(i)
        
    for i in range(len(s)):#괄호를 회전하기 위해서 큐이용해서 계속 돌리기.
        #print(q)
        if save(q)==1:#함수에서 된다는 뜻에 1이 오면 answer+=1
            answer+=1
        q.append(q.popleft())

    return answer

def save(state):# 
    stack=[] 
    for i in state: #스택 이용
        if not stack:#만약 아무것도 없으면 스택에 넣고
            stack.append(i)
        else:#있으면
            if i=='[' or i=='(' or i=='{':#만약 이것들이면 넣고
                stack.append(i)
            else:#아니면 빼서 비교
                a=stack.pop()
                if a=='[':
                    if i!=']':
                        return 0
                    
                elif a=='(':
                    if i!=')':
                        return 0
                    
                elif a=='{':
                    if i!='}':
                        return 0  
                else:
                    return 0
    else:
        if not stack:#스택에 아무것도 없으면
            return 1#가능한거
        else:
            return 0#불가능한거