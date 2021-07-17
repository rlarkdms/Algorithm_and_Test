import copy
global num
num=987654321
#그리고 중요한게 여기서는 범위가 되게 좁기 때문에 그냥 돌았지만
#만약 범위가 크다면 재귀를 돌릴 수 있을지 모르고
#돌린다면 import sys sys.setrecursionlimit(10000) 추가해주는게 좋음.
def solution(begin, target, words):
    answer = 0
    recursion(begin,target,words,0)
    if num==987654321:#한번도 begin==target인 부분이 없을때는 return 0
        return 0
    else:
        return num#한번이라도 매칭되는 부분이 있으면 min에 의거해서 num을 return
    
def recursion(begin,target,words,count):
    global num
    print(words)
    if begin==target:#돌다가 begin이랑 target이랑 같을 때
        num=min(num,count)#가장 최소값을 구하는 것이니 min 내장함수로 이전 값하고 비교.
        return 0
    
    for i in range(len(words)):#이거 단어를 도는 거고
        standard=0
        for j in range(len(begin)):#스펠링하나하나를 비교하는 과정임.
            if begin[j]==words[i][j]:
                standard+=1
                
        if standard==len(begin)-1:#만약 하나 빼고 다 같다면 ==바꿀 수 있다는 뜻.
            copy_words=copy.copy(words) #words를 카피함 이유는 이 다음단어를 돌아야 하기 떄문이다.
            del copy_words[i]#여기서 해당 하나빼고 다 다른 문자열을 제거하고 다시 재귀로 호출
            recursion(words[i],target,copy_words,count+1)