def solution(s):
    answer = ''
    answer=answer+s[0].upper()#첫번째 글자는 무조건 대문자로하기
    for i in range(1,len(s)):
        if s[i-1]==' ':
            answer=answer+s[i].upper()#만약 공백이 나오면 그 다음 글자를 대문자로
        
        else:
            answer=answer+s[i].lower()#공백 이후가 아니면 소문자로
            
#여기서 중요한 발견 str은 appeend가 +로 이어 붙여야함!!!
    return answer