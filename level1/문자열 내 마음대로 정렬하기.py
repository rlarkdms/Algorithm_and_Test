def solution(strings, n):
    answer = []
    temp=""
    for i in range(0,len(strings)):
        for j in range(i+1,len(strings)):
            print(strings[i])
            if strings[i][n]>strings[j][n]:#strings에서 만약 크면 바꾸는데
                temp=strings[i]
                strings[i]=strings[j]
                strings[j]=temp
            elif strings[i][n]==strings[j][n]:#같으면 사전상 더 앞에 있으면 바꿈
                if strings[i]>strings[j]:
                    temp=strings[i]
                    strings[i]=strings[j]
                    strings[j]=temp
        
#이거 위치 바꾸는 코드를 def로 짰으면 더 좋았을 텐데...아 여기 포인터 있나?
    return strings