def solution(nums):
    answer = 0

    my_set=set(nums)
    my_list=list(my_set)
    #중복을 없애는 코드

    if len(my_list)<len(nums)/2:#문제를 읽어보니 중복을 제외하고 몇가지를 뽑을 수 있냐 이 얘기라서
        answer=len(my_list) #중복의 제외한 개수가 nums의 길이의 2분에 1이하이면 중복된 포켓몬 수 만큼
    else:
        answer=len(nums)/2 #아니면 뽑을 수 있는 최대의 수 만큼.
#이 문제를 쉽게 풀려면 
    return answer