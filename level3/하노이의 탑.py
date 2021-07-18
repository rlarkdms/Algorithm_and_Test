# 굉장히 간단한 문제임 규칙을 알면 바로 풀 수 있는 문제임.
# 일단 이 문제의 규칙은 이전에 있던 n에서 기반하여 연산하는건데.
# 간단히 말하자면 n이 2->3 으로 간다고 하면 
# n에 있던 가는 루트에서 기둥의 위치만 바꾸면 된다.
# 1.예를 들어 3->2 2->3으로 바꾸면 된다. 이러면 n-1까지의 원판을 2번 기둥으로 옮기게 되는 과정을 얻게 된다. 
# 2. 그 다음 [1,3]을 넣고(이유는 그마지막에 남아있던 n원판을 3번 기둥으로 옮기는 과정) 그리고 2번 기둥에있던 n-1까지의 원판으로 2번기둥에서 3번 기둥으로 옮기는 과정을 거치면 된다.
# 3. 2번기둥에서 3번기둥으로 옮기는거 또한 n-1번째에서 과정을 얻었기때문에 기둥의 숫자만 바꾸면 된다. 1->2 2->1로 그리고 배열에 삽입하면 완료!
def solution(n):
    answer = []
    example=[[1,2],[1,3],[2,3]]

    for count in range(2,n):# 몇 번째 원판까지 돌껀지에 대한 것.
        for i in range(len(example)):# swap이라고 해야하나? 기둥의 숫자 바꾸는 과정( 1번 과정)
            for j in range(len(example[i])):
                if example[i][j]==3:
                    example[i][j]=2
                elif example[i][j]==2:
                    example[i][j]=3
        example.append([1,3])# 2번 과정
        for i in range(len(example)-1):# 3번 과정인데 여기서는 편의를 위해 1->2 2->3 3->1 로 바꿨다.ㅎㅎ....
            arr=[]
            for j in range(len(example[i])):
                if example[i][j]==1:
                    arr.append(2)  
                elif example[i][j]==3:
                    arr.append(1)
                elif example[i][j]==2:
                    arr.append(3)
            example.append(arr)
   
    return example
