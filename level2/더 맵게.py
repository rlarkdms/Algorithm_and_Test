def solution(scoville, K):
    answer = 0
    confirm=0

    while True:
        scoville.sort()
        for i in scoville:
            if i<K:
               
                scoville.append((scoville.pop(1)*2)+(scoville.pop(0)))
                confirm+=1
                if len(scoville)==1:#저 -1조건을 충족하기 위해 필요.
                    if scoville[0]<K:
                        return -1
                break
        else:
            return confirm