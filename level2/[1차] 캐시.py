# 해당 도시와 맛집 게시물을 읽어보여주는 서비스를 개발하고 있다.
# 로직에 대한 성능 측정을 한다...
# DB 캐시의 성능 개선을 시도하고 있지만 크기를 얼마로 해야 효율적인지 알수없다.
# DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램을 작성.
# 캐시 크기(cacheSize)와 도시 이름 배열(cities)
# cities의 개수는 최대 100,000개 
# 도시 이름은 최대 20자
# Cachesize는 30 이하이다.
#LRU 알고리즘이 뭔지 모르는데 한번 구현해보자
# 범위가 그렇게 큰 편이 아님 그리고 cities의 크기도 큰 편이 아니라서 그냥 해도 될듯.
#from collections import deque
# 시간 조금이라도 줄일려고 큐로 하려고 했는데 큐는 중간에 pop이 안되네..ㅎㅎ... 
def solution(cacheSize, cities):
    answer = 0
    
    q=[]
    # if cacheSize==0:
    #     return len(cities)*5
    for i in cities:#cities를 도는데
        if i.lower() in q:#만약 배열안에 해당 값이 있으면 큐 hit이고 갱신을 위해 배열 가장 끝으로 가야지.
            q.pop(q.index(i.lower()))#그리고 .lower()이 있는 이유는 대소문자를 구분하지 않기 때문이다.
            q.append(i.lower())
            answer+=1#캐시 hit라서 +1
        else:#값이 없으면
            q.append(i.lower()) #값 더하기 캐시만큼 안찼을 때는 계속 더하는거고 
            if len(q)==cacheSize+1:#캐시 사이즈만큼 찼을 떄는 하나 뺴는 거고
                q.pop(0)#원래 코드는 len(q)==cacheSize 인데 0을 처리 못해서 이렇게 바꿈.
            #q.append(i.lower())
            answer+=5# 캐시 miss라서 +5
        
    return answer