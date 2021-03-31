def solution(s):
    answer = True

    s=s.lower()//소문자로 다 바꾸고

    print(s)

    if s.count("p")==s.count("y")://p의 개수 y의 개수
        answer = True//같으면 true 
    else:
        answer = False//다르면 false
    
    return answer