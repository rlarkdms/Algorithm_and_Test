def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if ord(s[i])==32:
            answer=answer+' '#공백이면 공백 더하기
        if 65<=ord(s[i])<=90:
            if ord(s[i])+n>90:
                answer=answer+chr(ord(s[i])+n-26)#대문자 중에 더해서 Z을 넘어가면 -26하고 다시 char로 바꾸기
            else:
                answer=answer+chr(ord(s[i])+n)
        if 97<=ord(s[i])<=122:
            if ord(s[i])+n>122:
                answer=answer+chr(ord(s[i])+n-26)#소문자 중에 더해서 z을 넘어가면 -26하기 
            else:
                answer=answer+chr(ord(s[i])+n)

            
    return answer