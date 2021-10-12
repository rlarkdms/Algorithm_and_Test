def solution(n):
    arr=[0]*(n+1)
    arr[2]=3
    sum_value=0
    for i in range(4,(n+1),2):
        sum_value+=arr[i-4]
        arr[i]=(arr[i-2]*3+sum_value*2+2)%1000000007#이게 새로운 패턴이 매번 2개씩 나타나고 그 2번째 전꺼에서 *3를 해야하고 sum_value는 이전부터 오던거를 계속 더해서 *2해야함 이유는 2칸을 채우는 가지수 뿐만 아니라 4칸을 채울수있는 방법이 따로 존재하기 때문이다.      
    return arr[n]