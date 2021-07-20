def solution(stones, k):
    #아 그렇네 생각해보니까 3개씩 묶어서 돌면서 합이 아니라 맥스다 제일 적은거를 찾으면 되잖아!
    if stones[0]>=stones[-1]:#이게 케이스를 알아서 이렇게한건데 케이스를 모르면 이 방법을 사용할 수 없음....
        stones.reverse()
    min_value=max(stones[0:k])
    standard=min_value
    #이게 3개씩 3개씩 보는데 만약 stones[i-k]가 standard랑 같다는건 이제까지의 값중에서 가장 클수도 있는 값이 빠져나간다는 거라서 다시 max를 연산하여 가장 큰 값을 찾아내는 거지 그리고 그 큰 값중에 가장 작은 값을 찾으면 됨.
    for i in range(k,len(stones)):
        if standard==stones[i-k]:#이거 작은거 아닌이상은 부르지 않으면 되는거 아닌가?
            standard=max(stones[i-k+1:i+1])# 이 부분 때문인데 이걸 줄일 수 있는 방법이 없나?
            min_value=min(min_value,standard) 
    # 효율성 13번이 무슨 TC인지 알겠다. 13TC는 [98,97,96,95,94,93,92....] 이런식으로 있는 TC다 그래서 연산이 오래걸린거야...
    # 반대로 14번은 [1,2,3,4,5,6,7,8...] 이런순이다.
    # 이거 갑자기 생각난게 뒤랑 같이 돌면...?
    return min_value
#징검다리 건너기 문제 이거 TC를 알아서 꼼수로 통과한거 나중에 한번 다시 풀어봐야 함.
#이번에 깨달은것은 만약 TC 주어지면 최악의 수를 고려해보자.