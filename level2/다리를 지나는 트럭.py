from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge=deque()
    truck_weights.reverse()#pop(0)을 하면 시간오래 걸리기 때문에 Reverse한 다음 올려두기.
    count=0
    for i in range(bridge_length):
        bridge.append(0)
    sum_value=0
    while True:
        
        if not truck_weights:#truck_weights가 없어지면 끝난 거임.
            count+=bridge_length
            break
        if sum_value+truck_weights[-1]-bridge[0]<=weight:
            standard=truck_weights.pop()# 트럭의 값을 빼고
            bridge.append(standard)#넣고를 반복
            sum_value-=bridge.popleft()#sum_value를 뺴기
            sum_value+=standard
            count+=1
        else:
            sum_value-=bridge.popleft()
            bridge.append(0)
            count+=1     
        
    return count