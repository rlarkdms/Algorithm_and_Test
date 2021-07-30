def solution(p):
    answer = ''
    #입력이 빈 문자열이면 빈 문자열을 반환한다.
    #이거 일단 스택 문제임.
    print(u_v(p,answer))
    return answer
def u_v(u,statement):#재귀적으로 돌리는 함수.
    left=0
    right=0
    for i in range(len(u)):
        if u[i]=='(':
            left+=1
        elif u[i]==')':
            right+=1
        
        if left==right:
            print(u[:i+1])
            print(u[i+1:])
            left=0
            right=0
            if confirm(u[:i+1])==1:#올바른 괄호임.#여기가 u이고
                
                statement+=u[:i+1]
                print("문자열 %s" %(statement))
                if len(u[:i+1])!=0:
                    u_v(u[i+1:],statement)
                
                break
            else:#올바르지 않은 문자열이면 
                statement+="("
                statement+=u_v(u[i+1:],statement)
                statement+=")"
                statement+=reverse(u[1:i-1])
                break
    print("statement %s" %(statement))          
    return statement          
            
def reverse(statement):#문자열 뒤집기
    line=""
    for i in statement:
        if i==")":
            line+="("
        else:
            line+=")"
    
    return line
    

def confirm(arr):# 올바른지 확인하는 함수
    stack=[]
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