import heapq
def solution(operations):
    answer =[]
    for i in operations:
        if i[0]=='I':#힙에 넣기
            heapq.heappush(answer,int(i[2:]))
        elif i=='D 1'and len(answer)>0:#최댓값 삭제
            answer.pop()
        elif i=='D -1'and len(answer)>0:#최솟값 삭제
            heapq.heappop(answer)
            
    if len(answer)>0:
        return [max(answer),min(answer)]
    else:
        return [0,0]
