def solution(s):
    answer = True
    confirm=[]
    
    for i in s:
        if i=='(':#만약 '('이면
            confirm.append('(')#배열 안에 넣고
        elif i==')':#')'이면 
            if not confirm:#배열 확인해서 비였으면 False
                return False
            confirm.pop()#그리고 하나 빼기
    
    if len(confirm)>0:#나와서 배열길이가 0이 아니면 
        answer=False#False!

            
    return answer