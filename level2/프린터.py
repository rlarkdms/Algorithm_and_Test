def solution(priorities, location):
    newarr=[0]*len(priorities)#배열 크기만큼 선언 
    newresult=[]
    result=[]
    #내 생각 이거 완전 잘못 짰는데... 아 이걸 어떻게 해결해야할지 몰라서 그냥 쓴다...
    #그니까 여기서 중요한건 location 2->C return 첫번째 라서 1를 return
    newarr[location]=1#location의 순서는 1로 대입
    
    while len(priorities)!=0 :#끝까지 도는데...
        for i in range(0,priorities.index(max(priorities))):#0~가장 큰숫자까지 도는데
            newarr.append(newarr.pop(0))#도는 동안 append
            priorities.append(priorities.pop(0))#도는 동안 append
   
            print(priorities)
       
        newresult.append(newarr.pop(0))#위에 for문이 다 돌면 맨 앞에 0번째는 배열에 넣음 그러면 하나하나 정리됨.
        result.append(priorities.pop(0))
          
    return newresult.index(1)+1