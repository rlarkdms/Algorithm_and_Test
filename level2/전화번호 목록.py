def solution(phone_book):
    answer = True

    #길이에 따라 정렬하기
    phone_book.sort(key=len)
    print(phone_book)
    #"12","88","123","567","1235" 이런식으로 정렬 길이에 따라...

    #그런 다음에 앞에꺼랑 비교해서 차례차례해서 접두사를 위해 0~len(phone_book[i])랑 앞에 껏들이랑 비교.
    for i in range(len(phone_book)):
        for j in range(i+1,len(phone_book)):
            if phone_book[i] == phone_book[j][0:len(phone_book[i])]:            
                answer=False
                break
        if answer==False:#이건 효율성을 위해 돌다가 False나오면 빠져나오기.
            break
    
    return answer