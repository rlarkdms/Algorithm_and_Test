import math
def solution(w,h):
    first,value,temp=0,0,0
    
    if w>h:#for문이 w의 길이를 기준으로 도는거라서 상대적으로 값이 작은걸로 가야한다. 이유는 1억 이하라...
        temp=w
        w=h
        h=temp
    
    for i in range(1,w+1):
        value=value+math.ceil(i*h/w)-int(first)
        first=i*h/w
        
        if i*h/w==int(i*h/w):
            break
    value=value*(w/i)
    
    return w*h-value
