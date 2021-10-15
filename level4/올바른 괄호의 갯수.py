def solution(n):
    # 카탈린 수 문제임 일단 점화식 같은게 있다는 뜻임.
    #이게 이미 정해져 있음 공식이
    # C0 =1 , Cn= 시그마 i=0부터 N까지 Ci*Cn-1 임.
    #https://jjycjnmath.tistory.com/139
    #n+2각형을 N개의 삼각형으로 나누는 방법도 카탈린 수 
    arr=[1]*(n+2)
    
    # N이 0일 떄는 -> 1
    # N이 1일 때는 -> 1 
    # 1*1 = 1
    # N이 2일 때는 -> 2
    # 1*1+1*1 = 2
    # N이 3일 때는 -> 5
    # 1*2+1*1+2*1 = 5
    standard=1
    while True:
        first=0#기준이 되는 수 set
        last=standard-1
        sum_value=0#합하기 위한 sum_value 정의
        for i in range(standard):
            sum_value+=(arr[first]*arr[last])#여기가 C0*C3+C1*C2+C2*C1+C3*C0
            first+=1 # first+=1
            last-=1 # last-=1
        arr[standard]=sum_value
        if standard==n: #standard==n일 때 break -> 이게 원하는 숫자가 되었을 때 그만! 멈춰!
            break
        standard+=1

    return arr[n]