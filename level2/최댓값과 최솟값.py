def solution(s):
    confirm=[]
    count=''
    for i in s: #계속 도는데
        if i==' ':
            confirm.append(int(count))#그걸 배열에 넣고
            count=''#count값 초기화
        else:#공백이 나타나지 않으면 숫자 더하기
            count=count+i
    else:
        confirm.append(int(count))#저게 돌다보면 마지막은 배열을 못 만나서 배열에 못들어가게 되는데 그때 들어갈 수 있게 해줌.
        
    return str(min(confirm))+' '+str(max(confirm))