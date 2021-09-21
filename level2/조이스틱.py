def solution(name):
    answer = 0
    #이게 여러가지 생각해야함....
    # A면 안바꿔도 되고, A말고 다른거면 바꾸기.
    # A위치가 제일 중요함.
    
    #위치 몇번 바꾸는 지
    for i in range(len(name)):
        if ord(name[i])<=78:
            answer+=(ord(name[i])-65)
            #print(name[i],(ord(name[i])-65))
        else:
            answer+=(91-ord(name[i]))
            #print(name[i],(91-ord(name[i])))
    
    # BBBABBABBB ->10개 짜리
    # BBBABBBAB  ->9개 짜리
    # BBABBA   BBBBA BBBBB BBBBB BBBBB
    #반으로 나누고 반 앞쪽에만 A가 있을 경우에는 
    arr=[]
    #4세션으로 나누고
    #2까지는 방법을 둬야겠구나....
    if len(name)==1:
        return answer
    if len(name)==2:
        if name[1]=='A':
            return answer
        else:
            return answer+1
    
    #4가지 방법이 있음.
    # 1) 그냥 계속 쭉 가는거 -> 거의 일반적인 방법일거임.
    for i in range(len(name)-1,0,-1):
        if name[i]!='A':
            arr.append(i)
            break
    #print(arr)

    # 2) 왼쪽으로 쭉가는거   -> 두번째가 A일 경우
    for i in range(1,len(name)):
        if name[i]!='A':
            arr.append(len(name)-i)
            break
    #print(arr)
    if len(name)>4:
    # 3) 오른쪽으로 갔다가 왼쪽으로 가는거 #이런 경우가 되는 특수경우를 가려내야함...#중간이 A가 쭉 있는 경우...
        for i in range(2,len(name)):
            if name[i]=='A':
                for k in range(i,len(name)):
                    if name[k]!='A':
                        arr.append((((i-1)*2))+len(name)-k)
                        break        
                #arr.append((((i-1)*2))+len(name)-k)
                break
          
    
    # 4) 왼쪽으로 갔다가 오른쪽으로 가는거.
    #사실 이 문제 다 해봐도 되긴하는데...하하...
        for i in range(len(name)-2,-1,-1):
            if name[i]=='A':
                for k in range(i,-1,-1):
                    if name[k]!='A':
                        #print(k)
                        arr.append((((len(name)-1-i)*2))+k)
                        break        
                #arr.append((((i-1)*2)+1)+len(name)-k)
                break
    
    #print(arr)    
    
    return answer+min(arr)