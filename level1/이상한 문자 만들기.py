def solution(s):
    answer = ''
    buffer=1
    for i in s:#문자열 다 돈다.
        if i==' ':
            buffer=1
            answer=answer+' '#공백이면 buffer 1로 바꾸고 다 더하기 
        elif buffer%2==1:
            buffer+=1
            answer=answer+i.upper()#홀수면 대문자
        elif buffer%2==0:
            buffer+=1
            answer=answer+i.lower()#짝수면 소문자
            
    return answer