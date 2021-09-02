import itertools
def solution(relation):
    answer = 0
    arr=[]
    for i in range(len(relation[0])):# 조합을 위한 리스트
        arr.append(i)
        
    answer_arr=[]
    for k in range(1,len(relation[0])+1):#여기가 그 조합을 위한 돌림판 1개만 선택할때 2개만 선택할 때 등등
        result = list(itertools.combinations(arr,k))#그래서 조합을 만들기 (1,2),(1,3) 이런식으로
        for i in result:
            sentence=[]
            for k in range(len(relation)):
                word=""
                for j in i:
                    word+=relation[k][j]#숫자나 문자들을 다 붙이기
                sentence.append(word)# 다 붙여서 word
            if len(sentence)==len(set(sentence)):#중복되는거 있으면 유일성이 해치는 거니까 버리고 중복되는게 없으면
                answer_arr.append(list(i))#answer_arr에 넣기.

    for i in range(len(answer_arr)):# answer_arr를 돌면서 
        for j in range(i+1,len(answer_arr)):
            if answer_arr[i]==[-1]:# 많이 돌지 말라는 의미에서...
                break
            if len(set(answer_arr[i])-set(answer_arr[j]))==0:#차집합해서 남는게 없으면
                answer_arr[j]=[-1]#중복된게 들어있는거니까 그냥 값을 임의로 바꾸기
    # 이게 뭔 말이냐면 [0] [0,1] [0,2] [0,3] [1,2] [0,1,2] [0,1,3] [1,2,3] 이런식으로 유일성을 만족하는 속성의 집합이 있다.
    # 이제는 최소성을 만족시켜야하는데 그렇게 하기 위해서는 앞에서 부터 중복되는게 있는지 보는것이다.
    # 예를 들어 [0]에 관련돼서는 [0,1] [0,2] [0,3] [0,1,2] [0,1,3] 이 없어진다. 그런데 여기서 pop이나 del을 하면 문제가 생기니
    # value를 그냥 일정값인 -1로 바꾸는 과정을 거친다.
    # 그러면 [0] [-1] [-1] [-1] [1,2] [-1] [-1] [1,2,3] 이 되고 그 뒤에 -1이 아닌 [1,2]를 가지고 루프를 돌면
    # [0] [-1] [-1] [-1] [1,2] [-1] [-1] [-1] 이 완성된다.
     
    for i in answer_arr:# 그 중 [-1]이 아닌 것을 고르면 된다.
        if i!=[-1]:
            answer+=1
         
    return answer