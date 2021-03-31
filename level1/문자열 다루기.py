def solution(s):
    answer = True
    
    for i in s:
        if len(s)==4 or len(s)==6:
            if i.isalpha()://알파벳 있으면 false
                print(i)
                answer=False
        else:
            answer=False//4 OR 6 이 아니면 false

    return answer