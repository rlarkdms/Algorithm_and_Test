def solution(a):
    answer=0
    #힙의 복잡도가 미쳐있는데....
    #근데 여기서 a의 수는 모두 다르다가 쫌 좋은 관점인데....
    # 내가 생각했던 방법인 오른쪽의 가장 작은 값을 구하고 그 값이 나오면 다시 update하는건 큰 문제점이 하나 있음 그건....만약 수의 배치가 
    # 1,2,3,4,5...이런식으로 올라가면 연산을 계속 해야하는 문제가 일어날 수 있음...음 일단 해볼까?
    # 해당 풀이는 시간초과가 남.    
    if a==1:
        return 1
    if a==2:
        return 2

    answer=2
    min_left=a[0]
    min_right=a[-1]
    min_left_arr=[]
    min_right_arr=[]
    for i in range(1,len(a)-1):
        min_left_arr.append(min_left) 
        if min_left>a[i]:#이 부분은 아마 맞을 거야.1~돌면서 가장 작은 값을 고르기 이렇게 한 이유는 루틴을 한번만 돌고서 해결하기가 어려웠음...
            min_left=a[i]
            
    for j in range(len(a)-2,0,-1):# 그래서 두개의 루틴을 가지고 해결을 도모함 왼쪽에서 오는 최솟값과 오른쪽에서 오는 최솟값 
        min_right_arr.append(min_right)
        if min_right>a[j]:
            min_right=a[j]
        
    for k in range(len(min_left_arr)):#그중 왼쪽의 최솟값과 오른쪽의 최솟값중을 비교해서 둘다 원값보다 작으면 될수 없는 상황이니 그것에 맞춰 조건 수정.
        if min_left_arr[k]>a[1+k] or min_right_arr[len(min_left_arr)-1-k]>a[1+k]:
            answer+=1

    return answer
