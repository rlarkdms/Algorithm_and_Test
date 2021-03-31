def solution(phone_number):
    answer = ""
    
    
    for i in range(0,len(phone_number)-4):#0~phone_number-4까지 *을 더하고
        answer=answer+"*"
    for j in range(len(phone_number)-4,len(phone_number)):
        answer=answer+phone_number[j]#phone_number-4~phone_number 까지는 숫자를 더하기


    return answer