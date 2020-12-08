def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge=[0]*(bridge_length-1)
    time=1
    while True:
        if not truck_weights and not bridge: #만약 배열 둘 다 비여있으면 break
            print(time)
            break
    
        if not truck_weights:#배열이 비여있으면
            bridge.pop(0)#무조건 빼기만
            #print(bridge)
            time+=1
        else:#truck_weight안에 값이 있으면
            if sum(bridge)+truck_weights[0]<=weight:
                bridge.pop(0)
                bridge.append(truck_weights.pop(0))
                time+=1
            else:
                bridge.pop(0)
                bridge.append(0)
                time+=1
        
        
    
    return time

#하나가 효율성을 통과 못함 고쳐야함...ㅠ