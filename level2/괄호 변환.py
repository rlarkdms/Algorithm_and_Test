def solution(p):
    answer=""
    
    return u_v(p,answer)
def u_v(u,statement):#재귀적으로 돌리는 함수.
    left=0
    right=0
    for i in range(len(u)):#u와 v를 가를 수 있는 숫자 세는 것.
        if u[i]=='(':
            left+=1
        elif u[i]==')':
            right+=1
    
        if left==right:#u와 v를 가를 수 있음.
            if confirm(u[:i+1])==1:#올바른 괄호임.#여기가 u이고 올바른 괄호면 그 뒤를 그냥 이어서 하기
                statement=statement+u[:i+1]+u_v(u[i+1:],statement)
                break
            else:#올바르지 않은 문자열이면 "("+뒤에 v를 다시 1번 부터 재귀로 돌리고+")"+나머지 문자열의 괄호 방향을 뒤집어서 붙이기.
                statement=statement+"("+u_v(u[i+1:],statement)+")"+reverse(u[1:i])
                break         
    return statement          
            
def reverse(statement):#문자열 뒤집기 ")"->"("  / "("->")"
    line=""
    for i in statement:
        if i==")":
            line+="("
        else:
            line+=")"
    
    return line
    
def confirm(arr):# 올바른지 확인하는 함수
    stack=[] #스택을 이용하여 올바른 괄호 문자열인지 확인.
    for i in arr:
        if i=='(':
            stack.append(i)
        if i==")":
            if len(stack)==0:   
                return 0
            stack.pop()
    else:
        if len(stack)==0:
            return 1
        else:
            return 0
