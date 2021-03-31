import math
def solution(n):
    answer = 0
    dou=0
    dou = math.sqrt(n)#루트 사용하는데
    if int(dou)**2==n:#만약 루트 제곱이랑 n값이랑 같으면 제곱근이니 +1해서 제곱함. 
        answer=int(dou+1)**2
    else:
        answer=-1#아니면 -1 넣기 
  
    return answer