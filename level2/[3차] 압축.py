#LZW 압축?
def solution(msg):
    answer = []
    arr=[]
    for i in range(26):
        arr.append(chr(i+65))
    standard=0
    while True:
        if standard>len(msg)-1:#standard를 끝내면 break
            break
        for j in range(len(arr)-1,-1,-1):#for 문을 계속 돌기.
            if msg[standard:].find(arr[j])==0:#만약 글자중 넣을 수 있으면 넣고 아님 말고 
                arr.append(msg[standard:standard+len(arr[j])+1])#사전 추가하는것
                standard+=len(arr[j])#현재 입력이 어디서 부터 시작될지 고르는 것
                answer.append(j+1)# return 값에 넣기
                break
 
    return answer