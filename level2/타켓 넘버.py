arr=0#전역 변수로 선언.
def solution(numbers, target):
    i,val=0,0
    global arr
    arr=0
    BFS(i,val,numbers, target)
    
    return arr
def BFS(i,val,numbers, target):#재귀 함수로 푸는것.
    global arr#이게 return answer의 역할을 하는 변수
    if i>=len(numbers):#numbers의 배열을 계속 돌다가 끝까지 돌았을때
        if target==val:#val 더한 값이랑 target이랑 똑같으면 arr+=1을 하여 return 값 올림.
            arr+=1
            return True
        else:
            return False
    BFS(i+1,val+numbers[i],numbers, target)#플러스 하는 것 하나
    BFS(i+1,val-numbers[i],numbers, target)#마이너스 하는 것 하나