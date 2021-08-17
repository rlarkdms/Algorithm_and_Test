def solution(enroll, referral, seller, amount):
    answer = []
    dict={}
    dict_money=[]
    dict_answer={}
    
    for i in range(len(enroll)):#일단 잇는 창구를 만들어주기... Ex) ['mary']='center' , ['edward']='mary' 이런식으로 해당 노드에 위값을 넣어주기.
        dict_answer[enroll[i]]=0#이건 각 노드마다 얻을 수 있는 수익을 넣어주기 위한 딕셔너리 설계
        if referral[i]=='-':#만약 맨 위에 'center'면 따로 'center'라고 지정해주기
            dict[enroll[i]]="center"
        else:
            dict[enroll[i]]=referral[i]#아니면 그냥 그 상위 노드를 값으로 넣어주기.
        
    for i in range(len(seller)):#seller을 안에 넣기 이거 처음에는 중복이 있다고 해서 중복을 다 더해야하는 줄 알고 딕셔너리로 설계했는데 질문하기를 보니까 중복이 있으면 따로 처리라는 말을 듣고 배열로 바꿈.
        dict_money.append([seller[i],amount[i]*100])

    for i in range(len(dict_money)):#여기서 연산을 시작하는데
        people=dict_money[i][0]#초기값을 정하고
        pay=dict_money[i][1]
        while True:
            dict_answer[people]+=(pay-(pay//10))# pay-(pay//10)으로 연산
            if dict[people]=='center':#맨 상위 노드에 닿으면 나가기 이유는 answer에 맨 상위노드인 center에 대한 값은 필요가 없음.
                break
                
            if (pay//10)<1:#만약 값이 1이하면 그만 더이상 상위노드로 갈 수 없음.
                break
            
            pay=pay//10#연산을 이어서 하기위해 값을 계속 수정하면서 루틴 돌기.
            people=dict[people]

    for i in dict_answer:#연산이 끝내 값들을 append 해서 배열에 저장.
        answer.append(dict_answer[i])

    return answer