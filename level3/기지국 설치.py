import math#올림 내장함수를 쓰기 위한 모듈
def solution(n, stations, w):
    answer = 0
    length=(2*w)+1#기지국의 커버리지 길이
    value=0#연산을 위한 value            
    for i in stations:#주어진 Stations리스트 돌기.
        if i-w<=1:#만약 i-w이 0보다 작으면 그냥 값을 1로 정의 
            a=1
        else:
            a=i-w
        answer+=math.ceil((a-value-1)/length)
        if i+w>=n:# 만약 i+w의 값이 n과 같거나 크면 n으로 정의
            value=n
        else:
            value=i+w
    else:
        answer+=math.ceil((n-value)/length)#여기는 돌다가 뒤에 남은 빈 집들의 연산을 위해 존재.
    return answer    
    
