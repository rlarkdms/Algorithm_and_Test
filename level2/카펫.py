def solution(brown, yellow):
    answer = []
    brown=brown/2#브라운을 반갈죽함.
    stand=0
    for i in range(1,int(brown)-1):
        stand=brown-i#이게 규칙 생각해서 하면 이렇게 됨. 설명하기 어려움....
        if yellow==((stand-2)*i):
            answer.append(stand)
            answer.append(i+2)
            break

    return answer