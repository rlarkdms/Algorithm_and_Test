#최소 필요 피로도 -> 해당 던전을 탐험하기 위해 가지고 있어야 하는 최소한의 피로도를 나타낸다.
#소모 피로도 -> 던전을 탐험한 후 소모되는 피로도를 나타낸다.

#한 유저가 이 던전들을 최대한 많이 탐험하려 한다.
# 유조가 탐험 할 수 있는 최대 던전 수를 Return하는 Solution 함수를 완성해라.
# K-> 현재 피로도.
# dungeons -> 행,던전의 개수
#아 여기서 중요한건 최소 필요 피로도와,소모 피로도는 같을 수 있습니다.
# 아 근데 이문제는 사실 저 세로의 길이가 1000 단위였으면 어려운 문제인데... 개수가 8이하...음...완전으로 돌아도 문제 없을 정도의
import itertools
def solution(k, dungeons):
    length=len(dungeons)
    answer = -1
    arr=list(itertools.permutations(dungeons,length))
    for i in range(len(arr)):
        min_value=k
        standard=0
        for j in arr[i]:
            if j[0]<=min_value:
                min_value-=j[1]
                standard+=1
            else:#덜 하면 그냥 나가리..
                break
        answer=max(answer,standard)
    return answer