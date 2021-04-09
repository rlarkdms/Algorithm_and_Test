global zero#개수를 세기위해서 global로 선언
zero=0
global one#개수를 세기위해서 global로 선언
one=0
def solution(arr):
    global zero
    global one
    answer = []
    compression(arr,0,len(arr),0,len(arr))#재귀로간다.
    answer.append(zero)
    answer.append(one)
    return answer

def compression(arr,afirst,alast,bfirst,blast):
    global zero
    global one
    word=arr[afirst][bfirst]#들어온 첫번째값을 기준으로 잡고 

    standard=True
    for i in range(afirst,alast):#그 부분들을 다 돌려돌려 돌림판
        for j in range(bfirst,blast):
            if arr[i][j]!=word:#만약 첫번째값이랑 다른게 나오면 바로 break
                standard=False
                break
        if standard==False:#위에 break문을 적용시키기위해 standard 변수와 함께 써서 break문 처리
            break
    else:#만약 첫번째값과 모든 값이 다 같다면 값에 따라 0,1인지 넣기
        if word==0:
            zero+=1
        else:
            one+=1
        return 0 #모든 값은 언젠가 여기 구문에 들어올테니 return 0

    #재귀로 오른쪽 상단하단 왼쪽 상단하단 다 돌기.
    compression(arr,afirst,alast-int((alast-afirst)/2),bfirst,blast-int((blast-bfirst)/2))#왼쪽 상단
    compression(arr,afirst+int((alast-afirst)/2),alast,bfirst,blast-int((blast-bfirst)/2))#오른쪽 상단
    compression(arr,afirst,alast-int((alast-afirst)/2),bfirst+int((blast-bfirst)/2),blast)#왼쪽 하단
    compression(arr,afirst+int((alast-afirst)/2),alast,bfirst+int((blast-bfirst)/2),blast)#오른쪽 하단
    return 0