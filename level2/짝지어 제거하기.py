def solution(s):
    answer = -1
    # 이 문제은 절대 pop(i)을 쓰면 안됨 문자열의 길이가 1,000,000이하 일 때인데...
    # stack 문제였구나...
    
    stack=[]
    for i in s:
        if not stack:#아무것도 없으면
            stack.append(i)# stack안에 넣어놓고
        else:
            if stack[-1]==i:# 맨 마지막이라 현재 값이랑 같으면
                stack.pop()# 맨 마지막꺼 빼버림
            else:
                stack.append(i)# 값 안같으면 stack에 넣어두기
    if not stack:# stack에 값이 없으면 return 1 다 짝이 맞는다는 얘기임.
        return 1
    else:# stack에 값이 있으면 짝을 못찾았다는 얘기임.
        return 0
